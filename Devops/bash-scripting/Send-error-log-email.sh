#!/bin/bash

# Scenario: I need to hit amazon.com url for 3 times if we dont have success response , capture the response in a error_log.tx file and send Email along with the file.


URL="https://amazon.com"
RETRY_COUNT=3
ERROR_LOG="error_log.txt"

# Email details
TO_EMAIL="your_email@example.com"
FROM_EMAIL="sender@yourdomain.com"
SUBJECT="[ALERT] Failed to access Amazon.com"

echo "Attempting to access $URL..."

for i in $(seq 1 $RETRY_COUNT); do
    HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
    
    if [ "$HTTP_STATUS" -eq 200 ]; then
        echo "Success! Received status code 200 on attempt $i."
        exit 0
    else
        echo "Attempt $i failed with status code $HTTP_STATUS."
        sleep 5  # Wait for 5 seconds before retrying
    fi
done

echo "All $RETRY_COUNT attempts failed. Capturing response and sending email."

# Capture the final response body in the error log file
curl -s "$URL" > "$ERROR_LOG"

# Send the email with the error log as an attachment
echo "The URL $URL could not be reached after $RETRY_COUNT attempts. Please see the attached error log for details." | \
mail -s "$SUBJECT" -r "$FROM_EMAIL" -a "$ERROR_LOG" "$TO_EMAIL"

echo "Email sent."
exit 1