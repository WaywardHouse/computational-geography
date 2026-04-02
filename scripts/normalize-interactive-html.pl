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

sub wrap_interactive_blocks {
  my ($text) = @_;
  my @lines = split /\n/, $text, -1;
  my @out;
  my $i = 0;
  my $fence;

  while ($i <= $#lines) {
    my $line = $lines[$i];

    if (defined $fence) {
      push @out, $line;
      if ($line =~ /^\Q$fence\E\s*$/) {
        undef $fence;
      }
      $i++;
      next;
    }

    if ($line =~ /^(~~~+|```+)/) {
      $fence = $1;
      push @out, $line;
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

my @files = @ARGV;
for my $file (@files) {
  open my $in, '<', $file or die "Unable to read $file: $!";
  local $/;
  my $original = <$in>;
  close $in;

  my $updated = wrap_interactive_blocks($original);
  next if $updated eq $original;

  open my $out, '>', $file or die "Unable to write $file: $!";
  print {$out} $updated;
  close $out;
  print "normalized $file\n";
}
