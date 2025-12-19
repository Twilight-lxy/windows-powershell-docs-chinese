---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamServerProvisioning.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/invoke-ipamserverprovisioning?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Invoke-IpamServerProvisioning
---

# 调用 IpamServerProvisioning 功能

## 摘要
自动化IPAM服务器的配置过程。

## 语法

### WID（默认值）
```
Invoke-IpamServerProvisioning [-WidSchemaPath <String>] [-ProvisioningMethod <ProvisioningMethod>]
 [-GpoPrefix <String>] [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 外部数据库（External Database）
```
Invoke-IpamServerProvisioning [-ProvisioningMethod <ProvisioningMethod>] [-GpoPrefix <String>] [-Force]
 [-DatabaseServer] <String> [-DatabaseName] <String> [-DatabasePort] <UInt16> [-DatabaseAuthType <AuthType>]
 [-DatabaseCredential <PSCredential>] [-UseExistingSchema] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Invoke-IpamServerProvisioning` cmdlet 用于在运行该 cmdlet 的主机上安装和配置 IP 地址管理 (IPAM) 服务器组件。无论您是在本地 IPAM 服务器上运行此 cmdlet，还是从远程站点通过 RSAT 远程执行它，该 cmdlet 都会将在当前会话所连接的 IPAM 服务器上安装并配置相应的 IPAM 组件。作为安装过程的一部分，该 cmdlet 会执行以下操作：

1. Configures the WCF and WSMan settings, such as Port and App Pool configuration.

2. Creates and connects to an IPAM database.
   The cmdlet attempts to create a database by using authentication credentials that the user specifies.
   An error occurs if the database that you specify does not exist or the chosen credentials do not include permissions to create a database.

3. Creates IPAM Tasks to get data for IPAM views.

4. Creates default user roles for access control.
   This includes RBAC roles in the database and any local security groups.

5. Configures a provisioning method.

6. By default, the cmdlet enables all available IPAM optional capabilities.

您可以手动或自动地为托管服务器配置访问权限。如果您是通过组策略来配置这些托管服务器的，请确保使用 **Invoke-IpamGpoProvisioning** cmdlet 在每个托管域中创建相应的 GPO（Group Policy Object）。

## 示例

### 示例 1：配置一个 IPAM 服务器
```
PS C:\> Invoke-IpamServerProvisioning
This cmdlet will provision IPAM on ipam1.contoso.com. As a part of provisioning, this cmdlet will provision IPAM to use Windows Internal database.
The cmdlet will create a new IPAM database at %WINDIR%\System32\IPAM\Database, create roles, and prepare IPAM for use.
Infrastructure servers managed by IPAM will have to be manually provisioned to provide access to IPAM. Read the product documentation for details.
Do you want to continue? Y
```

此命令为 IPAM 服务器配置了默认设置。默认情况下，IPAM 服务器使用 Windows 内部数据库（Internal Database），该数据库文件存储在默认路径 %WINDIR%\System32\IPAM\Database 中。管理下的服务器默认是通过手动方式进行配置的。

### 示例 2：配置一个 IPAM 服务器以使用基于 GPO 的资源分配功能
```
PS C:\> Invoke-IpamServerProvisioning -WidSchemaPath "D:\database" -ProvisioningMethod Automatic -GpoPrefix IPAM1
This cmdlet will provision IPAM on ipam1.contoso.com. As a part of provisioning, this cmdlet will provision IPAM to use Windows Internal database.
The cmdlet will create a new IPAM database at D:\database, create roles, and prepare IPAM for use.
IPAM will be configured to use Group Policy to provision the managed servers. Read the product documentation for details.
Do you want to continue?Y
```

此命令配置了一台 IPAM 服务器，使其使用 Windows 内部数据库以及基于 GPO 的配置方法来管理服务器。该命令将数据库文件存储在自定义的位置。

### 示例 3：配置一个 IPAM 服务器以使用 Microsoft SQL Server
```
PS C:\> Invoke-IpamServerProvisioning -DatabaseServer "Db1.Contoso.com" -DatabaseName "Ipamdb" -DatabasePort 1433
This cmdlet will provision IPAM on ipam1.Contoso.com. As a part of provisioning, this cmdlet will provision IPAM to use Microsoft SQL Server on Db1.Contoso.com.
The cmdlet will create a new IPAM database, create roles, and prepare IPAM for use.
Infrastructure servers managed by IPAM will have to be manually provisioned to provide access to IPAM. Read the product documentation for details.
Do you want to continue?
```

此命令配置了一台 IPAM 服务器，使其能够使用位于名为 Db1.Contoso.com 的数据库服务器上的 Microsoft SQL Server 数据库。示例假设存在这样一台服务器：Db1.Contoso.com，该服务器已安装了 Microsoft SQL Server；同时还有一个名为 Ipamdb 的空数据库实例，并且 IPAM 服务器具有对该数据库实例的访问权限。

### 示例 4：配置一个 IPAM 服务器，以便使用由 IPAM 提供的 Microsoft SQL Server 数据库
```
PS C:\> $Credential = Get-Credential
PS C:\> Invoke-IpamServerProvisioning -DatabaseServer "Db1.Contoso.com" -DatabaseName "Ipamdb" -DatabasePort 1433 -ProvisioningMethod Automatic -GpoPrefix IPAM1 -DatabaseAuthType SQL -DatabaseCredential $Credential
This cmdlet will provision IPAM on ipam1.contoso.com. As a part of provisioning, this cmdlet will provision IPAM to use Microsoft SQL Server on db1.contoso.com.
The cmdlet will create a new IPAM database, create roles, and prepare IPAM for use.
IPAM will be configured to use Group Policy to provision the managed servers. Read the product documentation for details.
Do you want to continue?
```

第一个命令使用 **Get-Credential** cmdlet 来获取凭据，并将结果存储在 `$Credential` 变量中。

第二个命令配置了一个 IPAM 服务器，使其使用位于名为 Db1.Contoso.com 的数据库服务器上的 Microsoft SQL Server 数据库。该示例假设存在一个名为 Db1.Contoso.com 的服务器，并且该服务器已安装了 Microsoft SQL Server；在 IPAM 进行配置的过程中会创建一个数据库实例。此外，IPAM 服务器具有以下权限：db_datawriter、db_datareader、db_ddladmin，以及查看数据库状态和修改数据库权限的权限。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
指定在连接到 IPAM 数据库时使用的身份验证类型。如果选择“Windows”作为身份验证类型，IPAM 将使用服务器计算机账户来连接数据库；如果是通过 SQL 身份验证，则需要提供用户名和密码才能连接到数据库。

```yaml
Type: AuthType
Parameter Sets: ExternalDatabase
Aliases:
Accepted values: Windows, SQL

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DatabaseCredential
用于指定运行 SQL Server 的计算机的凭据，该凭据以 **PSCredential** 对象的形式提供。要获取一个 **PSCredential** 对象，可以使用 **Get-Credential** cmdlet。有关更多信息，请输入 `Get-Help Get-Credential`。

```yaml
Type: PSCredential
Parameter Sets: ExternalDatabase
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
Parameter Sets: ExternalDatabase
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DatabasePort
指定 IPAM 服务器用于连接数据库服务器的端口。

```yaml
Type: UInt16
Parameter Sets: ExternalDatabase
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DatabaseServer
指定数据库服务器的完全合格域名（FQDN）或 IP 地址。您可以提供 IPv4 或 IPv6 地址，或者一个完全合格的域名（FQDN）。

```yaml
Type: String
Parameter Sets: ExternalDatabase
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需询问用户确认。

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

### -GpoPrefix
指定一个唯一的组策略对象（GPO）前缀名称，IPAM 使用该名称来创建组策略对象。仅当 *ProvisioningMethod* 参数的值为 “Automatic” 时，才使用此参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProvisioningMethod
指定手动或自动的、基于 GPO 的配置方式。该参数的可接受值为：Automatic（自动）和 Manual（手动）。在采用手动配置的情况下，您需要手动配置被管理的服务器以使其能够访问 IPAM（IP Address Management）。如果采用基于 GPO 或自动化的配置方式，则需要通过 **Invoke-IpamGpoProvisioning** cmdlet 在每个被管理的域中创建相应的 GPO（Group Policy Objects）。如果您未指定配置方法，系统将默认采用手动配置方式。

```yaml
Type: ProvisioningMethod
Parameter Sets: (All)
Aliases:
Accepted values: Automatic, Manual

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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

### -UseExistingSchema
表示 IPAM 服务器使用数据库服务器上已存在的模式（即不创建新的模式）。如果指定了此标志，但在服务器上找不到有效的模式，则会发生错误。

```yaml
Type: SwitchParameter
Parameter Sets: ExternalDatabase
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

### -WidSchemaPath
指定 IPAM 服务器上用于创建 Windows 内部数据库（WID）模式的位置。如果要使用现有的模式，请提供包含该模式文件的文件夹的路径。如果未为此参数指定值，IPAM 会尝试在默认路径 `%SystemDrive%\Windows\System32\ipam\Database` 下创建模式。

```yaml
Type: String
Parameter Sets: WID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Windows PowerShell中的IP地址管理（IPAM）服务器 cmdlet](./ipamserver.md)

