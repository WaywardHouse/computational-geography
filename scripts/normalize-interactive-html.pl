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
  return 1 if $block =~ /class="model-controls"/;
  return 1 if $block =~ /class="controls"/;
  return 1 if $block =~ /class="button-group"/;
  return 1 if $block =~ /class="info-panel"/;
  return 1 if $block =~ /class="(?:[a-z0-9-]+-info)"/;
  return 1 if $block =~ /<div\b[^>]*data-(?:leaflet|viz|map|d3)\b/;
  return 1 if $block =~ /^\s*<fieldset\b/m;
  return 1 if $block =~ /^\s*<label\b/m;
  return 1 if $block =~ /^\s*<input\b/m;
  return 1 if $block =~ /^\s*<select\b/m;
  return 1 if $block =~ /^\s*<canvas\b/m;
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

sub is_interactive_start_line {
  my ($line) = @_;

  return 1 if $line =~ /^\s*<label\b/;
  return 1 if $line =~ /^\s*<input\b/;
  return 1 if $line =~ /^\s*<select\b/;
  return 1 if $line =~ /^\s*<canvas\b/;
  return 1 if $line =~ /^\s*<fieldset\b/;
  return 1 if $line =~ /^\s*<script\b/;
  return 1 if $line =~ /^\s*<div\b[^>]*class="(?:viz-container|pyodide-cell|model-controls|controls|button-group|info-panel|[a-z0-9-]+-info)"/;
  return 1 if $line =~ /^\s*<div\b[^>]*data-(?:leaflet|viz|map|d3)\b/;

  return 0;
}

sub collect_interactive_sequence {
  my ($lines_ref, $start) = @_;
  my @lines = @$lines_ref;
  my $j = $start;
  my $depth = 0;
  my $saw_interactive = 0;

  while ($j <= $#lines) {
    my $candidate = $lines[$j];

    last if !$saw_interactive && $candidate =~ /^\s*$/;
    if ($saw_interactive && $depth <= 0 && $candidate =~ /^\s*$/) {
      last;
    }

    $saw_interactive = 1 if is_interactive_start_line($candidate);

    $depth += count_matches($candidate, qr/<div\b/);
    $depth -= count_matches($candidate, qr/<\/div>/);
    $depth += count_matches($candidate, qr/<fieldset\b/);
    $depth -= count_matches($candidate, qr/<\/fieldset>/);
    $depth += count_matches($candidate, qr/<label\b/);
    $depth -= count_matches($candidate, qr/<\/label>/);
    $depth += count_matches($candidate, qr/<script\b/);
    $depth -= count_matches($candidate, qr/<\/script>/);

    $j++;

    last if $saw_interactive && $depth <= 0 && ($j > $#lines || $lines[$j] =~ /^\s*$/);
  }

  return if !$saw_interactive || $j <= $start;

  my @block_lines = @lines[$start .. $j - 1];
  my $block = join("\n", @block_lines);
  return unless should_wrap_block($block);

  return ($j, \@block_lines);
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

    if (is_interactive_start_line($line)) {
      my ($j, $block_lines_ref) = collect_interactive_sequence(\@lines, $i);
      if (defined $j && defined $block_lines_ref) {
        my $block = dedent_html_block(join("\n", @$block_lines_ref));
        push @out, '```{=html}';
        push @out, split /\n/, $block, -1;
        push @out, '```';
        $i = $j;
        next;
      }
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
          $block = dedent_html_block($block);
          push @out, '```{=html}';
          push @out, split /\n/, $block, -1;
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
  return ();
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
