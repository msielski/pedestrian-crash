#!/bin/bash

# Convert all DOT Data to CSV format.

for filename in data/2001-2016/*.csv; do
  case "$filename" in
    *"Accidents"*)
      layout=accidents-old
      ;;
    *"Drivers"*)
      layout=drivers-old
      ;;
    *"Occupants"*)
      layout=occupants-old
      ;;
    *"Pedestrians"*)
      layout=pedestrians-old
      ;;
    *"Vehicles"*)
      layout=vehicles-old
      ;;
  esac
  clean_filename="${filename}.clean.csv"
  echo "Starting conversion of ${filename}."
  python3 ./parse.py "$filename" "$layout" "$clean_filename" &
done

for filename in data/2017-latest/*.csv; do
  case "$filename" in
    *"Accidents"*)
      layout=accidents-new
      ;;
    *"Drivers"*)
      layout=drivers-new
      ;;
    *"Occupants"*)
      layout=occupants-new
      ;;
    *"Pedestrians"*)
      layout=pedestrians-new
      ;;
    *"Vehicles"*)
      layout=vehicles-new
  esac
  clean_filename="${filename}.clean.csv"
  echo "Starting conversion of ${filename}."
  python3 ./parse.py "$filename" "$layout" "$clean_filename" &
done

echo
echo "Waiting for jobs to finish."
wait $(jobs -p)

echo
echo "Done with all jobs."
