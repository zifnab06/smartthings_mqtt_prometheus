# smartthings-mqtt-bridge prometheus exporter

Set up https://github.com/stjohnjohnson/smartthings-mqtt-bridge. Run server.py and get metrics from mqtt at localhost:9094/metrics.

Numeric values are exported as guages. String values (on/off/active/inactive) report as gauges with values 1/0.

## TODO

- configuration
- Add more metric types
