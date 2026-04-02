#!/usr/bin/env perl
use strict;
use warnings;

sub count_matches {
  my ($text, $pattern) = @_;
  my $count = 0;
  while ($text =~ /$pattern/g) {
    $count++;
  }
  return $count;
}

sub should_wrap_block {
  my ($block) = @_;

  return 1 if $block =~ /class="viz-container"/;
  return 1 if $block =~ /class="pyodide-cell"/;
  return 1 if $block =~ /^\s*<script\b/m;

  return 0;
}

sub is_interactive_html_fence {
  my ($info) = @_;
  return defined $info && $info =~ /^\{=html\}\s*$/;
}

sub should_normalize_fenced_html {
  my ($block) = @_;
  return should_wrap_block($block)
    || $block =~ /class="controls"/
    || $block =~ /class="button-group"/
    || $block =~ /class="info-panel"/
    || $block =~ /class="(?:[a-z0-9-]+-info)"/
    || $block =~ /<canvas\b/
    || $block =~ /<label\b/
    || $block =~ /<select\b/
    || $block =~ /<input\b/;
}

sub dedent_html_block {
  my ($block) = @_;
  my @lines = split /\n/, $block, -1;
  my $min_indent;

  for my $line (@lines) {
    next if $line =~ /^\s*$/;
    next unless $line =~ /^([ \t]+)/;
    my $indent = length($1);
    $min_indent = $indent if !defined($min_indent) || $indent < $min_indent;
  }

  return $block unless defined $min_indent && $min_indent > 0;

  for my $line (@lines) {
    $line =~ s/^[ \t]{0,$min_indent}// if $line =~ /\S/;
  }

  return join("\n", @lines);
}

sub wrap_interactive_blocks {
  my ($text) = @_;
  my @lines = split /\n/, $text, -1;
  my @out;
  my $i = 0;
  my $fence;
  my $fence_marker;
  my @fence_lines;

  while ($i <= $#lines) {
    my $line = $lines[$i];

    if (defined $fence) {
      if (is_interactive_html_fence($fence) && $line =~ /^\Q$fence_marker\E\s*$/) {
        my $block = join("\n", @fence_lines);
        if (should_normalize_fenced_html($block)) {
          $block = dedent_html_block($block);
        }
        push @out, "${fence_marker}${fence}";
        push @out, split /\n/, $block, -1;
        push @out, $fence_marker;
        undef $fence;
        undef $fence_marker;
        @fence_lines = ();
        $i++;
        next;
      }

      if (is_interactive_html_fence($fence)) {
        push @fence_lines, $line;
        $i++;
        next;
      }

      push @out, $line;
      if ($line =~ /^\Q$fence_marker\E\s*$/) {
        undef $fence;
        undef $fence_marker;
      }
      $i++;
      next;
    }

    if ($line =~ /^(~~~+|```+)(.*)$/) {
      $fence_marker = $1;
      $fence = $2 // '';
      if (is_interactive_html_fence($fence)) {
        @fence_lines = ();
      } else {
        push @out, $line;
      }
      $i++;
      next;
    }

    if ($line =~ /^\s*<div\b/) {
      my $j = $i;
      my $depth = 0;
      my $saw_div = 0;

      while ($j <= $#lines) {
        my $candidate = $lines[$j];
        $depth += count_matches($candidate, qr/<div\b/);
        $depth -= count_matches($candidate, qr/<\/div>/);
        $saw_div = 1 if $candidate =~ /<div\b/;
        $j++;
        last if $saw_div && $depth <= 0;
      }

      if ($saw_div && $depth <= 0) {
        my $k = $j;
        while ($k <= $#lines && $lines[$k] =~ /^\s*$/) {
          $k++;
        }

        if ($k <= $#lines && $lines[$k] =~ /^\s*<script\b/) {
          $j = $k;
          while ($j <= $#lines) {
            my $candidate = $lines[$j];
            $j++;
            last if $candidate =~ /<\/script>\s*$/;
          }
        }

        my @block_lines = @lines[$i .. $j - 1];
        my $block = join("\n", @block_lines);

        if (should_wrap_block($block)) {
          push @out, '```{=html}';
          push @out, @block_lines;
          push @out, '```';
          $i = $j;
          next;
        }
      }
    }

    push @out, $line;
    $i++;
  }

  return join("\n", @out);
}

sub audit_interactive_blocks {
  my ($text) = @_;
  my @issues;

  while ($text =~ /```+\{=html\}\n(.*?)\n```/sg) {
    my $block = $1;
    next unless should_normalize_fenced_html($block);
    next unless $block =~ /^\s{2,}<(?:(?:label|input|select|canvas|button|p|span|div)\b)/m;
    push @issues, 'indented-html-in-raw-fence';
  }

  return @issues;
}

my @files = @ARGV;
for my $file (@files) {
  open my $in, '<', $file or die "Unable to read $file: $!";
  local $/;
  my $original = <$in>;
  close $in;

  my @issues = audit_interactive_blocks($original);
  if (@issues) {
    print "audit $file: ", join(', ', @issues), "\n";
  }

  my $updated = wrap_interactive_blocks($original);
  next if $updated eq $original;

  open my $out, '>', $file or die "Unable to write $file: $!";
  print {$out} $updated;
  close $out;
  print "normalized $file\n";
}
