#!/bin/bash

echo "launching database"
launch_db_res=$(oci db system launch --compartment-id $COMPARTMENT_ID \
--availability-domain $AVAILABILITY_DOMAIN \
--subnet-id $SUBNET_ID \
--shape BM.DenseIO2.52 --cpu-core-count 4 --database-edition STANDARD_EDITION \
--hostname cli-db-host --admin-password Adm11n_Pwd_ --db-name clidb --db-version 11.2.0.4 \
--ssh-authorized-keys-file $SSH_KEY_FILE --node-count 1 \
--recovery-window-in-days 30 --auto-backup-enabled false \
--domain cli.oraclecorp.com --wait-for-state AVAILABLE | \
grep -v "Action completed" 2>/dev/null)
echo $launch_db_res

db_system_id=$(jq -r '.data.id' <<< ${launch_db_res})
echo "db_system_id=$db_system_id"

echo "terminating db system"
oci db system terminate --db-system-id $db_system_id --force
