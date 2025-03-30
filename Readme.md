# foosball table
### Description
This project aims to make it fun to run a hobby foosballtable season. It allows for random team selection and keeps the scores of all the players across multiple seasons.

## Build and Run
`cd foosballtable && docker build -t foosballtable .  && docker run --network=host --volume ./:/foosballtable docker.io/library/foosballtable`
