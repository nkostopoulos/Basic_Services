10.0.0.2 -> NTP server
10.0.0.1 -> client allowed to sync
others pcs -> not allowed to sync

service ntp restart -> restart ntp service
ntpq -r -> shows servers synced with client. The star indicates that the client is allowed to query the server.
