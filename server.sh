#!/bin/sh

while true; do
  nohup python server >> test.out
done &
