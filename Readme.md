# foosball table

# Build
`cd foosballtable && docker build -t foosballtable .`

# Run
`cd foosballtable && docker run --network=host --volume ./:/foosballtable docker.io/library/foosballtable`