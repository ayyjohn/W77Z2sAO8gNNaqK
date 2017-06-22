"""Our team wants to offer customers the ability to request on-demand
showings where a showing agent drives to a chosen property at a certain
time and shows the property to potential buyers. To create the system that
routes requests to agents whoa re nearby we need to know the driving distance
from a given showing agent's location to the given property. The team is
considering using the Google Distance Matrix API. Create a wrapper that makes
the API easy to use, as a minimal implementation have it take as arguments

- a single origin, an address formatted as a string, e.g. "2301 Hyperion Ave,
Los Angeles, CA 90027
- a single destination formatted in the same way
- a time of departure formatted as a standard date or time object

and have the wrapper return a number that represents the driving
distance in miles. Additionally, if you were going to continue implementing
a more feature rich version of this wrapper what other features would be useful?"""


# other features: fuzzy searching or more lenient auto parsing of inputs

import urlsp
