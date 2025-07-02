# Configuración de MySQL
db_config = {
    "host": "192.168.2.48",
    "user": "base_llama",
    "password": "llama_nec",
    "database": "logs_stash"
}


# schema_description = """
# Table: switch_logs2

# Columns:
# - timestamp (DATETIME): Date and time when the event occurred.
# - switch_name (VARCHAR): Name of the switch.
# - ip_address (VARCHAR): IP address of the switch.
# - log_level (VARCHAR): Severity level of the log message. Possible values:
#     - 'emergency': System is unusable
#     - 'alert': Action must be taken immediately
#     - 'critical': Critical conditions
#     - 'error': Error conditions
#     - 'warning': Warning conditions
#     - 'notice': Normal but significant condition
#     - 'info': Informational messages
#     - 'debug': Debug-level messages
# - event (TEXT): Description of the log event.
# - conecction_ssh_ip (VARCHAR): IP address used for SSH connection.
# - conecction_ssh_port (INT): Port used for SSH connection.
# - ssh_status (VARCHAR): SSH connection status (e.g., active, down).
# - brand (VARCHAR): Brand or manufacturer of the switch.
# - device_type (VARCHAR): Type of device (e.g., core, access).
# """


schema_description = """
Table: switch_logs2

Columns:
- timestamp (DATETIME): Date and time when the event occurred.
- switch_name (VARCHAR): Name of the switch.
- ip_address (VARCHAR): IP address of the switch.
- log_level (VARCHAR): Severity level of the log message. Possible values include:

    Code | Level         | Description
    -----|---------------|---------------------------------------------------------------
    0    | Emergency     |  Emergency: the system is completely unusable.
    1    | Alert         |  Alert: immediate action is required.
    2    | Critical      |  Critical: severe failure in a key component.
    3    | Error         |  Error: a failure that prevents proper functioning.
    4    | Warning       |  Warning: potential issue that may lead to an error.
    5    | Notice        |  Notice: important event, not an error.
    6    | Informational |  Informational: normal operations logging.
    7    | Debug         |  Debug: technical details for development and diagnostics.

- event (TEXT): Description of the log event.
- conecction_ssh_ip (VARCHAR): IP address used for the SSH connection.
- conecction_ssh_port (INT): Port number used for the SSH connection.
- ssh_status (VARCHAR): SSH connection status (e.g., active, down).
- brand (VARCHAR): Brand or manufacturer of the switch.
- device_type (VARCHAR): Type of device (e.g., core, access).
"""
