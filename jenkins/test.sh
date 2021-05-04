#!/bin/bash
res=$(curl -s -w "%{http_code}" $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' testing-nginx)/sum/4/2)
body=${res::-3}
if [ "$body" != "5" ]; then
  echo "Error"
fi
