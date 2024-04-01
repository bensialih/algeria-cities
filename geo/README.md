
# django Algeria geolocation
## Motivation
a requirement for geolocation for the communes/wilayas in Algeria

## Approach/Problem
initial simple google co-ordinates could have surfice, however I quickly realised that taking the "north-east" to "south-west" co-ordinates of a place that was, say, C-shaped would have included a large portion of territory that was not part of that jurisdiction

## Solution
Postgis has polygon that is a list of co-ordinates where it allows you more accurate drawing of borders
Furthermore, the ability to use said co-ordinates to get distance, location within the polygon area and so forth can be very helpful in getting a more acurate picture of a location relative to another.
