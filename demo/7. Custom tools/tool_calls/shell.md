---
host: localhost
participants:
  shell:
---

cd into /tmp and list the files
print the current date

make 2 two separate calls

**shell**

###### Steps

- Run Shell Command [1] `{"command": "cd /tmp && ls"}`
- Run Shell Command [2] `{"command": "date"}`

###### Execution: Run Shell Command [1]

<pre>
CalNotificationsAvailable
com.apple.CoreSimulator.SimDevice.99316E9E-C449-4CAE-9F40-9780601BB51D
com.apple.CoreSimulator.SimDevice.E6B1C3FE-5931-4088-B023-5583DC3A851D
com.apple.launchd.2Abp4KitYD
com.apple.launchd.GPZoOkh1bl
com.apple.launchd.IMKXPOfs53
com.apple.launchd.K2ICX0F2fy
com.apple.launchd.PJiJW5sGGr
com.apple.launchd.PsycLSX1NQ
com.apple.launchd.QJb33aerGC
com.apple.launchd.ZUaEv94t3u
com.apple.launchd.bvzek0a7nU
com.apple.launchd.gImSC4qd3m
com.apple.launchd.pURPxOBX8m
mysql.sock
mysqlx.sock
textmate-501.sock

Exit Code: 0
</pre>

###### Execution: Run Shell Command [2]

<pre>
Sun Mar 31 17:01:18 +04 2024

Exit Code: 0
</pre>

**shell** The first command successfully listed the files in the `/tmp` directory, showing various system and application-related temporary files, including `mysql.sock`, `mysqlx.sock`, and `textmate-501.sock` among others.

The second command successfully printed the current date, which is `Sun Mar 31 17:01:18 +04 2024`.

**user**

cd into /tmp and list the files
print the current date

make 2 two separate calls

**shell**

###### Steps

- Run Shell Command [1] `{"command": "cd /tmp && ls"}`
- Run Shell Command [2] `{"command": "date"}`

###### Execution: Run Shell Command [1]

<pre>
CalNotificationsAvailable
com.apple.CoreSimulator.SimDevice.99316E9E-C449-4CAE-9F40-9780601BB51D
com.apple.CoreSimulator.SimDevice.E6B1C3FE-5931-4088-B023-5583DC3A851D
com.apple.launchd.2Abp4KitYD
com.apple.launchd.GPZoOkh1bl
com.apple.launchd.IMKXPOfs53
com.apple.launchd.K2ICX0F2fy
com.apple.launchd.PJiJW5sGGr
com.apple.launchd.PsycLSX1NQ
com.apple.launchd.QJb33aerGC
com.apple.launchd.ZUaEv94t3u
com.apple.launchd.bvzek0a7nU
com.apple.launchd.gImSC4qd3m
com.apple.launchd.pURPxOBX8m
mysql.sock
mysqlx.sock
textmate-501.sock

Exit Code: 0
</pre>

###### Execution: Run Shell Command [2]

<pre>
Sun Mar 31 17:01:57 +04 2024

Exit Code: 0
</pre>

