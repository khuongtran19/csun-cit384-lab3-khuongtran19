#!/bin/bash

# Emit the HTTP response header
echo "X-function: Emitting a hereis document"
echo "Content-type: text/json"


# Emit a blank line to separate the HTTP response header from the HTTP response body 
echo ""


# Emit the HTTP response body
cat <<EOF
<!-- Start of the Body -->
<html>
  <head>
     <title>Hello!</title>
  </head>
  <body>
    <h1>A Simple HTML Document</h1>
    "Hello!"
  </body>
</html>
<!-- End of the Body -->
EOF
