This is upload funtion for api Gateway with lambda
important points to remember

1. requet content-type should match with binary settingson api Gateway.
2. integration request on api gatewya with lambda would need VTL template updates.
3. decrypting of binary needs to be done on lambda.
4. deployment of gateway before changes are applied.
5. you can integrated direct s3 to api too. 