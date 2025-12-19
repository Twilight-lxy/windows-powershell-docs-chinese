---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDatabase.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamdatabase?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamDatabase
---

# 设置 Ipam 数据库

## 摘要
修改 IPAM 用于连接到 IPAM 数据库的设置。

## 语法

```
Set-IpamDatabase [-DatabaseServer] <String> [-DatabaseName] <String> [-DatabasePort] <UInt16>
 -DatabaseAuthType <AuthType> [-DatabaseCredential <PSCredential>] [-PassThru] [-Force]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-IpamDatabase` cmdlet 用于修改 IP 地址管理（IPAM）所使用的配置设置，这些设置决定了 IPAM 如何连接到托管在运行 Microsoft SQL Server 的计算机上的 IPAM 数据库。

请确认您可以从 IPAM 服务器访问数据库服务器。请指定是使用托管 IPAM 服务器的计算机上的账户进行连接，还是使用 SQL Server 数据库账户进行连接。如果您指定了 IPAM 服务器账户，请确保该账户具有必要的权限。

使用 `Get-IpamDatabase` cmdlet 来查看数据库配置设置。

您可以指定任何端口来连接数据库服务器。我们建议您使用默认端口（1433）来连接 Microsoft SQL Server。

## 示例

### 示例 1：连接到外部数据库
```
The first command command uses the **Get-IpamDatabase** cmdlet to display the configuration settings of the database.
PS C:\> Get-IpamDatabase
DatabaseType     : WID
WidSchemaPath    : C:\Windows\System32\IPAM\Database
DatabaseServer   :
DatabaseName     : IPAM
DatabasePort     :
DatabaseAuthType : Windows
DatabaseUser     :


The second command sets the database configuration. The command includes the database name and database server name. The cmdlet prompts you before it continues.
PS C:\> Set-IpamDatabase -DatabaseServer "ContosoDB04" -DatabaseName "IpamData01" -DatabasePort 1433 -DatabaseAuthType Windows
Confirm
Updating IPAM database settings to use an MsSql database. If the configuration is successful, IPAM cannot be
reconfigured to use Windows Internal Database.  The cmdlet will verify that the database specified is reachable and
compatible with Ipam version. Do you want to continue?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y

The last command repeats the first command, displaying the revised configuration information.
PS C:\> Get-IpamDatabase
DatabaseType     : MSSQL
WidSchemaPath    :
DatabaseServer   : ContosoDB04
DatabaseName     : IpamData01
DatabasePort     : 1433
DatabaseAuthType : Windows
DatabaseUser     :
```

这个示例配置了 IPAM 服务器以连接到外部数据库。该命令不会从现有的 Windows 内部数据库（WID）中移动任何数据，也不会创建新的数据库。所有访问设置都需要在数据库服务器上手动进行配置。示例中使用 Windows 作为数据库的身份验证类型。

## 参数

### -AsJob
将该cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行该cmdlet之前，会提示您进行确认。

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
指定用于连接到运行 SQL Server 的计算机的身份验证类型。该参数的可接受值包括：

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
用于指定运行 SQL Server 的计算机的凭据，该凭据以 **PSCredential** 对象的形式提供。要获取一个 **PSCredential** 对象，请使用 **Get-Credential** cmdlet。有关更多信息，请输入 `Get-Help Get-Credential`。

如果您为 *DatabaseAuthType* 参数指定了 SQL Server 的值，请指定此参数。

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
指定一个 SQL Server 数据库的名称。IPAM 服务器会连接到该数据库。

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
指定 IPAM 服务器用于连接到数据库服务器的端口号。

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
指定数据库服务器的完全限定域名（FQDN）或 IP 地址。IPAM 服务器将连接到该服务器。

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
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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
该参数用于指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最优限制值。这个限制仅适用于当前正在运行的命令，而不适用于整个会话或整个计算机。

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
展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamDatabase
此 cmdlet 返回一个对象，该对象代表 IPAM 服务器的数据存储区（datastore）。

## 备注

## 相关链接

[Get-IpamDatabase](./Get-IpamDatabase.md)

[Move-IpamDatabase](./Move-IpamDatabase.md)

