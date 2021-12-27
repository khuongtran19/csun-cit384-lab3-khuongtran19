#!/bin/bash

USERNAME=${QUERY_STRING#*username=}
USERNAME=${USERNAME%%&*}
USERNAME=${USERNAME//+/ }

echo "Content-type: text/html"
echo ""
cat <<EOF
<html>
<head>
<title>user response</title>
</head>
<body>
<p>Here's what you said:</p>
<p>You entered ${USERNAME}</p>
</body>
</html>
EOF
