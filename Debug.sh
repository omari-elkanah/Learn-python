#!/bin/bash
echo -e 'Welcome to the basic calculator!'
echo -e 'Welcome to the basic calculator!' >> operation_history.txt


while true; do

  echo "Enter an arithmetic operation or type 'quit' to quit:"
  echo "Enter an arithmetic operation or type 'quit' to quit:" >> operation_history.txt


  read input
  echo "$input" >> operation_history.txt


  if [[ $input == 'quit' ]]; then
    echo 'Goodbye!'
    echo 'Goodbye!' >> operation_history.txt
    break
  fi


  if [[ $input =~ ^-?[0-9]+(\.[0-9]+)?\ [+-\\*/]\ -?[0-9]+(\.[0-9]+)?$ ]]; then

    result=$(echo "scale=2; $input" | bc)
    echo "$result"
    echo "$result" >> operation_history.txt
  else

    echo 'Operation check failed!'
    echo 'Operation check failed!' >> operation_history.txt
  fi
done