# ThingsBoard Modbus Drilling Rig Emulator

This is a simple modbus drilling rig emulator that can be used to test Modbus integration with platform using
ThingsBoard IoT Gateway.

## Devices

| Device       | Unit Id | Port |
|--------------|:--------|:----:|
| Drilling Bit | 1       | 5021 |
| Drilling Mud | 2       | 5022 |
| Drilling Rig | 3       | 5023 |
| Preventer    | 4       | 5024 |
| Drawwork     | 5       | 5025 |

### Drilling Bit

| Sensors                        | Default value | Modbus Register Type | Modbus Address |
|:-------------------------------|:-------------:|----------------------|---------------:|
| Bottom Hole Temperature Sensor |       0       | HR                   |              1 |
| Drill Bit Position Sensor      |       0       | HR                   |              2 |
| Drill Bit Vibration Sensor     |      20       | HR                   |              3 |
| Mud Pressure Sensor            |      25       | HR                   |              4 |
| ROP Sensor                     |       0       | HR                   |              5 |
| Well Depth Sensor              |               | HR                   |              6 |
| Running                        |     False     | CO                   |              1 |

### Drilling Mud

| Sensors                | Default value | Modbus Register Type | Modbus Address |
|:-----------------------|:-------------:|----------------------|---------------:|
| Gas Cut Mud Sensor     |      90       | HR                   |              1 |
| Mud Density Sensor     |      1.2      | HR                   |              2 |
| Mud Flow Rate Sensor   |      40       | HR                   |              3 |
| Mud Level Sensor       |      70       | HR                   |              4 |
| Mud Pressure Sensor    |      30       | HR                   |              5 |
| Mud Temperature Sensor |      50       | HR                   |              6 |
| Mud Volume Sensor      |      90       | HR                   |              7 |
| Running                |     False     | CO                   |              1 |

### Drilling Rig

| Sensors                          | Default value | Modbus Register Type | Modbus Address |
|:---------------------------------|:-------------:|----------------------|---------------:|
| Drilling Line Hoist Speed Sensor |       0       | HR                   |              1 |
| Hook Load Sensor                 |       0       | HR                   |              2 |
| Rotary Speed Sensor              |       0       | HR                   |              3 |
| Mud Pressure Sensor              |      15       | HR                   |              4 |
| Running                          |     False     | CO                   |              1 |

### Preventer

| Sensors                      | Default value | Modbus Register Type | Modbus Address |
|:-----------------------------|:-------------:|----------------------|---------------:|
| Equipment Temperature Sensor |       0       | HR                   |              1 |
| Equipment Vibration Sensor   |       0       | HR                   |              2 |
| Mud Temperature Sensor       |       0       | HR                   |              3 |
| Flow Rate Sensor             |       0       | HR                   |              4 |
| Gas Cut Mud Sensor           |       0       | HR                   |              5 |
| System Leak Detection Sensor |       0       | HR                   |              6 |
| Well Pressure Sensor         |       0       | HR                   |              7 |
| Running                      |     False     | CO                   |              1 |

### Drawwork

| Sensors             | Default value | Modbus Register Type | Modbus Address |
|:--------------------|:-------------:|----------------------|---------------:|
| Cable Length Sensor |       0       | HR                   |              1 |
| Hoist Speed Sensor  |       0       | HR                   |              2 |
| Inclination Sensor  |      10       | HR                   |              3 |
| Position Sensor     |      30       | HR                   |              4 |
| Tension Sensor      |      170      | HR                   |              5 |
| Vibration Sensor    |      15       | HR                   |              6 |
| Running             |     False     | CO                   |              1 |

## Gateway Modbus Connector Config

```json
{
  "logLevel": "DEBUG",
  "master": {
    "slaves": [
      {
        "host": "0.0.0.0",
        "port": 5035,
        "type": "tcp",
        "method": "socket",
        "timeout": 3,
        "byteOrder": "BIG",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "unitId": 1,
        "deviceName": "Drilling Bit",
        "deviceType": "default",
        "reportStrategy": {
          "type": "ON_CHANGE_OR_REPORT_PERIOD",
          "reportPeriod": 10000
        },
        "connectAttemptTimeMs": 3000,
        "connectAttemptCount": 3,
        "waitAfterFailedAttemptsMs": 30000,
        "attributes": [
          {
            "tag": "running",
            "type": "bit",
            "functionCode": 1,
            "objectsCount": 1,
            "address": 1
          },
          {
            "tag": "depth",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 6
          },
          {
            "tag": "rop",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 5
          }
        ],
        "timeseries": [
          {
            "tag": "temperature",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 1
          },
          {
            "tag": "position",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 2
          },
          {
            "tag": "vibration",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 3
          },
          {
            "tag": "pressure",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 4
          }
        ],
        "attributeUpdates": [
          {
            "tag": "rop",
            "type": "16int",
            "functionCode": 6,
            "objectsCount": 1,
            "address": 5
          },
          {
            "tag": "depth",
            "type": "16int",
            "functionCode": 6,
            "objectsCount": 1,
            "address": 6
          }
        ],
        "rpc": [
          {
            "tag": "setRunning",
            "type": "bit",
            "functionCode": 5,
            "objectsCount": 1,
            "address": 1
          }
        ]
      },
      {
        "host": "0.0.0.0",
        "port": 5036,
        "type": "tcp",
        "method": "socket",
        "timeout": 3,
        "byteOrder": "BIG",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 3000,
        "unitId": 2,
        "deviceName": "Drilling Mud",
        "deviceType": "default",
        "connectAttemptTimeMs": 3000,
        "connectAttemptCount": 3,
        "waitAfterFailedAttemptsMs": 30000,
        "attributes": [
          {
            "tag": "running",
            "type": "bit",
            "functionCode": 1,
            "objectsCount": 1,
            "address": 1
          },
          {
            "tag": "tankCapacity",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 7
          },
          {
            "tag": "opened",
            "type": "bit",
            "functionCode": 1,
            "objectsCount": 1,
            "address": 2
          }
        ],
        "timeseries": [
          {
            "tag": "gasCut",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 1
          },
          {
            "tag": "density",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 2,
            "divider": 10
          },
          {
            "tag": "flowRate",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 3
          },
          {
            "tag": "liquidVolume",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 4
          },
          {
            "tag": "pressure",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 5
          },
          {
            "tag": "temperature",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 6
          }
        ],
        "attributeUpdates": [],
        "rpc": [
          {
            "tag": "setRunning",
            "type": "bit",
            "functionCode": 5,
            "objectsCount": 1,
            "address": 1
          },
          {
            "tag": "setOpened",
            "type": "bit",
            "functionCode": 5,
            "objectsCount": 1,
            "address": 2
          }
        ]
      },
      {
        "host": "0.0.0.0",
        "port": 5037,
        "type": "tcp",
        "method": "socket",
        "timeout": 3,
        "byteOrder": "BIG",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "unitId": 3,
        "deviceName": "Drilling Rig",
        "deviceType": "default",
        "reportStrategy": {
          "type": "ON_CHANGE_OR_REPORT_PERIOD",
          "reportPeriod": 10000
        },
        "connectAttemptTimeMs": 3000,
        "connectAttemptCount": 3,
        "waitAfterFailedAttemptsMs": 30000,
        "attributes": [
          {
            "tag": "running",
            "type": "bit",
            "functionCode": 1,
            "objectsCount": 1,
            "address": 1
          }
        ],
        "timeseries": [
          {
            "tag": "lineHoistSpeed",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 1
          },
          {
            "tag": "hookLoad",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 2
          },
          {
            "tag": "speed",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 3
          },
          {
            "tag": "pressure",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 4
          }
        ],
        "attributeUpdates": [],
        "rpc": [
          {
            "tag": "setRunning",
            "type": "bit",
            "functionCode": 5,
            "objectsCount": 1,
            "address": 1
          }
        ]
      },
      {
        "host": "0.0.0.0",
        "port": 5038,
        "type": "tcp",
        "method": "socket",
        "timeout": 3,
        "byteOrder": "BIG",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "unitId": 4,
        "deviceName": "Preventer",
        "deviceType": "default",
        "reportStrategy": {
          "type": "ON_CHANGE_OR_REPORT_PERIOD",
          "reportPeriod": 10000
        },
        "connectAttemptTimeMs": 3000,
        "connectAttemptCount": 3,
        "waitAfterFailedAttemptsMs": 30000,
        "attributes": [
          {
            "tag": "running",
            "type": "bit",
            "functionCode": 1,
            "objectsCount": 1,
            "address": 1
          }
        ],
        "timeseries": [
          {
            "tag": "equipmentTemperature",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 1
          },
          {
            "tag": "vibration",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 2
          },
          {
            "tag": "mudTemperature",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 3
          },
          {
            "tag": "flowRate",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 4
          },
          {
            "tag": "gasCut",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 5
          },
          {
            "tag": "leak",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 6
          },
          {
            "tag": "pressure",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 7
          }
        ],
        "attributeUpdates": [],
        "rpc": [
          {
            "tag": "setRunning",
            "type": "bit",
            "functionCode": 5,
            "objectsCount": 1,
            "address": 1
          }
        ]
      },
      {
        "host": "0.0.0.0",
        "port": 5039,
        "type": "tcp",
        "method": "socket",
        "timeout": 3,
        "byteOrder": "BIG",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "unitId": 5,
        "deviceName": "Drawwork",
        "deviceType": "default",
        "connectAttemptTimeMs": 3000,
        "connectAttemptCount": 3,
        "waitAfterFailedAttemptsMs": 30000,
        "attributes": [
          {
            "tag": "running",
            "type": "bit",
            "functionCode": 1,
            "objectsCount": 1,
            "address": 1
          },
          {
            "tag": "direction",
            "type": "bit",
            "functionCode": 1,
            "objectsCount": 1,
            "address": 2
          },
          {
            "tag": "drawworkSpeed",
            "type": "bit",
            "functionCode": 1,
            "objectsCount": 1,
            "address": 3
          }
        ],
        "timeseries": [
          {
            "tag": "length",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 1
          },
          {
            "tag": "speed",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 2
          },
          {
            "tag": "inclination",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 3
          },
          {
            "tag": "position",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 4
          },
          {
            "tag": "tension",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 5
          },
          {
            "tag": "vibration",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": 6
          }
        ],
        "attributeUpdates": [],
        "rpc": [
          {
            "tag": "setRunning",
            "type": "bit",
            "functionCode": 5,
            "objectsCount": 1,
            "address": 1
          },
          {
            "tag": "setDirection",
            "type": "bit",
            "functionCode": 5,
            "objectsCount": 1,
            "address": 2
          },
          {
            "tag": "drawworkSpeed",
            "type": "bit",
            "functionCode": 5,
            "objectsCount": 1,
            "address": 3
          }
        ]
      }
    ]
  }
}
```

## Installation

1. Pull emulator docker image:
    ```bash
    docker pull thingsboard/tb-modbus-pool-emulator:latest
    ```
2. Run the emulator using the following command, which will start the emulator on ports 5021-5034:
    ```bash
    docker run --rm -d --name tb-modbus-pool-emulator -p 5021-5025:5021-5025 tb-modbus-pool-emulator
    ```
   ***Note***: *If you run the gateway first - it may take up to 2 minutes since the emulator starts to the gateway
   connects to it*.
3. Create a new gateway device in ThingsBoard and copy the access token.
4. Pull gateway image from Dockerhub using the following command:
    ```bash
    docker pull thingsboard/tb-gateway:latest
    ```
5. Replace YOUR_ACCESS_TOKEN with the access token of the gateway device and host (if you want to connect to
   ThingsBoard, not on your machine) in docker-compose.yml.
6. Run the gateway using the following command:
    ```bash
    docker-compose up
    ```
7. Add Modbus connector and configure the ThingsBoard IoT Gateway on UI to connect to the emulated devices. You can find
   configuration in *pool_connector.json*.
8. The gateway connects to emulated devices, creates them on the platform, starts receive data from devices and send it
   to ThingsBoard.
