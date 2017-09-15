<?php
  $a = 0;
  function IsPrime($n)
  {
      for($x=2; $x<$n; $x++)
      {
         if($n%$x ==0)
          {
           return 0;
          }
      }
    return 1;
  }

  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $a = $_POST["number"];
  }
  $res = IsPrime($a);
  if ($res==0)
  echo 'This is not a Prime Number.....'."\n";
  else
  echo 'This is a Prime Number..'."\n";
?>