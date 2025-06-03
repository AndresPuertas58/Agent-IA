# Configuración de MySQL
db_config = {
    "host": "192.168.2.48",
    "user": "base_llama",
    "password": "llama_nec",
    "database": "logs_stash"
}


schema_description = """
Table: switch_logs

Columns:
id (INT, PK): Unique log ID
timestamp(DATETIME): Date and time of the event
switch_id (INT) : Optional foreing key ID of the switch
switch_name (VARCHAR): Switch name
model (VARCHAR): Switch model (e.g, Cisco 2960)
ip_address (VARCHAR): IP address of the switch
log_level (VARCHAR):lOG LEVEL (INFO, WARN,ERROR)
event (TEXT): Event description
affected_port(VARCHAR): Affected port ( e.g., Gig1/0/1)
zone (VARCHAR): Logical/physical location of the switch
"""