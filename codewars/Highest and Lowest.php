<?php
# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/php

function highAndLow($numbers)
{
//   return "";
  $new = explode(' ', $numbers);
  $high = $new[0];
  $low = $new[0];
  foreach ($new as $value) {
    if($value > $high) {
        $high = $value;
    }
    if($value < $low) {
        $low = $value;
    }
  }
  echo "$high $low";
}

highAndLow("1 2 3 4 5");  // return "5 1"
highAndLow("1 2 -3 4 5"); // return "5 -3"
highAndLow("1 9 3 4 -5"); // return "9 -5"
