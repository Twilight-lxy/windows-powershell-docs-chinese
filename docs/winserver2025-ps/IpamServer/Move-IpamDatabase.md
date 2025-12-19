---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDatabase.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/move-ipamdatabase?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-IpamDatabase
---

# 移动 IPAM 数据库

## 摘要
将 IPAM 数据库迁移到 SQL Server 数据库中。

## 语法

```
Move-IpamDatabase [-DatabaseServer] <String> [-DatabaseName] <String> [-DatabasePort] <UInt16>
 -DatabaseAuthType <AuthType> [-DatabaseCredential <PSCredential>] [-PassThru] [-Force]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Move-IpamDatabase` cmdlet 将 IP 地址管理（IPAM）数据库迁移到 Microsoft SQL Server 数据库。您可以从中 Windows 内部数据库（WID）或现有的 SQL Server 数据库进行迁移。该 cmdlet 会创建一个新的 IPAM 架构，并将所有数据从现有的 IPAM 数据库中复制过来。在完成数据复制后，它会更改 IPAM 配置设置，以便使用新的数据库作为 IPAM 数据库。如果您是从 WID 进行迁移的，该 cmdlet 会在文件名后添加时间戳来重命名现有的数据和日志文件。

如果由于任何原因该cmdlet无法完成迁移操作，它会返回一个错误，并且不会更改当前的数据库设置。

请确认您可以从 IPAM 服务器访问数据库服务器。指定是使用托管 IPAM 服务器的计算机上的账户进行连接，还是使用 SQL Server 数据库账户进行连接。如果您选择了 IPAM 服务器账户，请确保该账户具有写入目标数据库所需的权限。如果迁移需要创建一个新的数据库，请确认该账户具有创建和写入该数据库的权限。

使用 `Get-IpamDatabase` cmdlet 来查看数据库配置设置。

我们建议您在迁移数据库之前，将 IPAM 服务器隔离出来，并关闭所有 IPAM 客户端。

源数据库和目标数据库的排序规则（collation）应该相同。如果目标数据库不存在，此 cmdlet 会使用目标 SQL Server 的默认排序规则来创建一个新的数据库。但如果源 SQL 数据库的默认排序规则与目标不同，可能会导致错误。为了避免这种情况，请按照以下步骤手动创建目标数据库。

从 WID 数据库迁移到外部 SQL Server 数据库

使用以下命令在外部 SQL Server 上创建目标数据库：

`CREATE DATABASE \[\<DBName\>\] COLLATE \<DB collation name\>`  
在这种情况下，参数 ‘DB collation name’ 应指定为 **SQL LATIN1_general_CP1_CI_AS**。

将数据从一个SQL Server数据库迁移到一个外部SQL Server数据库

使用以下命令读取现有数据库的排序规则（collation）：

`SELECT collation_name FROM sys.databases WHERE name = N'\<DBName\>'`

使用以下命令在目标SQL服务器上创建一个新的数据库：

`CREATE DATABASE \[\<DBName\>\] COLLATE \<DB collation name\>`

## 示例

### 示例 1：迁移 IPAM 数据库
```
This command uses the **Get-IpamDatabase** cmdlet to get the database configuration information. The console displays configuration information, including the type of database, WID.
PS C:\> Get-IpamDatabase
DatabaseType     : WID

WidSchemaPath    : C:\Windows\System32\IPAM\DataBase

DatabaseServer   :

DatabaseName     : IPAM

DatabasePort     :

DatabaseAuthType : Windows

DatabaseUser     :


This command moves the IPAM data to a database named IpamDB1 on the server named ContosoDB22. The database uses port 1433. The command specifies Windows as the authentication type, so the command uses credentials for the IPAM server. The cmdlet prompts you for confirmation.
PS C:\> Move-IpamDatabase -DatabaseServer "ContosoDB22" -DatabaseName "IpamDB1" -DatabasePort 1433 -DatabaseAuthType Windows
Confirm

This command will migrate IPAM data to the specified MsSql Database. The cmdlet will create a new Ipam Schema, copy the data and configure IPAM to use the new database. Once this migration is completed successfully, you will not be able to revert to using Windows Internal Database. Do you want to continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y


This command uses the **Get-IpamDatabase** cmdlet to get the database configuration information. The console displays configuration information, including the type of database, WID. The console displays configuration information, including the type of database, now MSSQL. The database now has values for **DatabaseServer**, **DatabaseName**, and **DatabasePort**, as specified in the second command.
PS C:\> Get-IpamDatabase
DatabaseType     : MSSQL

WidSchemaPath    :

DatabaseServer   : ContosoDB22

DatabaseName     : IpamDB1

DatabasePort     : 1433

DatabaseAuthType : Windows

DatabaseUser     :
```

这个示例将一个 IPAM 数据库迁移到名为 ContosoDB22 的数据库服务器上的一个名为 IpamDB1 的数据库中。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `-*Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -DatabaseAuthType
指定用于连接到运行 SQL Server 的计算机的身份验证类型。该参数的可接受值为：

- SQL.
Use the database account.
Specify this credential by using the *DatabaseCredential* parameter.
- Windows.
Use the account for the computer that runs the IPAM server.

```yaml
Type: AuthType
Parameter Sets: (All)
Aliases:
Accepted values: Windows, SQL

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DatabaseCredential
指定用于运行 SQL Server 的计算机的凭据，该凭据以 **PSCredential** 对象的形式提供。要获取一个 **PSCredential** 对象，请使用 **Get-Credential** cmdlet。有关更多信息，请输入 `Get-Help Get-Credential`。

如果您为 **DatabaseAuthType** 参数指定了一个 SQL 值，请指定此参数。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DatabaseName
指定一个 SQL Server 数据库的名称。该 cmdlet 会将 IPAM 数据库迁移到这个数据库中。如果目标服务器上不存在这个数据库，IPAM 会在该服务器上创建一个具有指定名称的新数据库。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DatabasePort
指定 IPAM 服务器用于连接到数据库服务器的端口。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DatabaseServer
指定数据库服务器的完全限定域名（FQDN）或 IP 地址。此 cmdlet 会将 IPAM 数据库迁移到该服务器上。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-IpamDatabase](./Get-IpamDatabase.md)

[Set-IpamDatabase](./Set-IpamDatabase.md)

