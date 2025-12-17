---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adreplicationsite?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADReplicationSite
---

# 新的AD复制站点

## 摘要
在目录中创建一个 Active Directory 复制站点。

## 语法

```
New-ADReplicationSite [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-AutomaticInterSiteTopologyGenerationEnabled <Boolean>] [-AutomaticTopologyGenerationEnabled <Boolean>]
 [-Credential <PSCredential>] [-Description <String>] [-Instance <ADReplicationSite>]
 [-InterSiteTopologyGenerator <ADDirectoryServer>] [-ManagedBy <ADPrincipal>] [-Name] <String>
 [-OtherAttributes <Hashtable>] [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>]
 [-RedundantServerTopologyEnabled <Boolean>] [-ReplicationSchedule <ActiveDirectorySchedule>]
 [-ScheduleHashingEnabled <Boolean>] [-Server <String>] [-TopologyCleanupEnabled <Boolean>]
 [-TopologyDetectStaleEnabled <Boolean>] [-TopologyMinimumHopsEnabled <Boolean>]
 [-UniversalGroupCachingEnabled <Boolean>] [-UniversalGroupCachingRefreshSite <ADReplicationSite>]
 [-WindowsServer2000BridgeheadSelectionMethodEnabled <Boolean>]
 [-WindowsServer2000KCCISTGSelectionBehaviorEnabled <Boolean>] [-WindowsServer2003KCCBehaviorEnabled <Boolean>]
 [-WindowsServer2003KCCIgnoreScheduleEnabled <Boolean>]
 [-WindowsServer2003KCCSiteLinkBridgingEnabled <Boolean>] [<CommonParameters>]
```

## 描述
**New-ADReplicationSite** cmdlet 用于在 Active Directory 复制环境中创建站点。在 Active Directory 中，站点的作用是：让客户端能够发现位于其计算机物理位置附近的网络资源（已发布的共享资源、域控制器），或者减少通过广域网 (WAN) 链路传输的数据流量。此外，站点还可以用来优化域控制器之间的数据复制过程。

## 示例

### 示例 1：创建一个复制站点
```powershell
PS C:\> New-ADReplicationSite -Name "NorthAmerica"
```

这个命令创建了一个名为“NorthAmerica”的新网站。

### 示例 2：创建一个复制站点并为其设置一个属性
```powershell
PS C:\> New-ADReplicationSite -Name "Europe" -AutomaticInterSiteTopologyGenerationEnabled $FALSE
```

此命令创建一个名为“Europe”的新站点，并将**AutomaticInterSiteTopologyGenerationEnabled**属性设置为该新站点的值。

### 示例 3：创建一个复制站点并设置其复制计划
```powershell
PS C:\> $Schedule = New-Object -TypeName System.DirectoryServices.ActiveDirectory.ActiveDirectorySchedule
PS C:\> $Schedule.ResetSchedule()
PS C:\> $Schedule.SetDailySchedule("Twenty","Zero","TwentyTwo","Thirty");
PS C:\> New-ADReplicationSite -Name "Asia" -ReplicationSchedule $schedule
```

这个示例创建了一个名为“Asia”的新站点，并将每日的复制任务（*ReplicationSchedule*）时间设置为从20:00到22:30。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

```yaml
Type: ADAuthType
Parameter Sets: (All)
Aliases:
Accepted values: Negotiate, Basic

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AutomaticInterSiteTopologyGenerationEnabled
该参数用于指示 cmdlet 是否会阻止 Knowledge Consistency Checker（KCC，即站点间拓扑生成器 ISTG）为站点间复制生成连接。当您希望创建手动建立的站点间连接（从而禁用 ISTG），同时保留 KCC 以生成站点内的连接时，请使用此选项。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AutomaticTopologyGenerationEnabled
该选项用于决定是否启用自动拓扑生成功能。如果启用此功能，KCC将不会在站点内的所有服务器之间自动生成连接。如果您使用手动配置的连接，并且不希望KCC自动构建这些连接，请禁用该选项。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您确认是否要执行该操作。

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

### -Credential
指定一个具有执行此操作权限的用户账户。默认值为当前用户。

请输入一个用户名，例如 User01 或 Domain01/User01；或者输入一个 **PSCredential** 对象（例如通过 **Get-Credential** cmdlet 生成的对象）。如果您输入了用户名，系统会提示您输入密码。

此参数不受任何随 Windows PowerShell 安装的提供程序的支持。

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

### -Description
用于指定对象的描述信息。此参数为对象的 **Description** 属性设置值。在轻量级目录访问协议（LDAP）中，该属性的显示名称（**ldapDisplayName**）即为 “description”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Instance
指定一个站点对象的实例，用作创建新站点对象的模板。

你可以使用现有的站点对象实例作为模板，也可以通过使用 Windows PowerShell 命令行或脚本来创建一个新的站点对象。

方法 1：使用现有的站点对象作为新对象的模板。要获取现有站点对象的实例，请使用 **Get-ADReplicationSite** cmdlet。然后将该站点对象提供给 **New-ADReplicationSite** cmdlet 的 *Instance* 参数，以创建一个新的站点对象。你可以通过设置适当的参数来覆盖新对象的属性值。

方法 2：创建一个新的 **ADReplicationSite**，并通过使用 Windows PowerShell 命令行界面来设置相应的属性值。然后将这个对象传递给 **New-ADReplicationSite** cmdlet 的 *Instance* 参数，以创建新的站点对象。

注意：指定的属性不会经过验证；因此，尝试设置不存在或无法设置的属性会引发错误。

```yaml
Type: ADReplicationSite
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InterSiteTopologyGenerator
指定作为该站点站点间拓扑生成器的服务器。

```yaml
Type: ADDirectoryServer
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ManagedBy
通过提供以下属性值之一来指定管理该对象的用户或组：

- Distinguished name
- GUID (objectGUID)
- Security identifier (objectSid)
- SAM account name (sAMAccountName)

注意：括号中的标识符是该属性在 LDAP 中显示的名称。

此参数设置了 Active Directory 属性，并为其指定一个 LDAP 显示名称“managedBy”。

```yaml
Type: ADPrincipal
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
为复制站点对象指定一个名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OtherAttributes
用于为那些没有通过 cmdlet 参数表示的属性指定对象属性值。您可以使用此参数同时设置一个或多个属性值。如果某个属性支持多个值，您可以为其分配多个值。要识别某个属性，请使用在 Active Directory 架构中为此属性定义的 LDAP 显示名称（**ldapDisplayName**）来进行标识。

要为某个属性指定一个单一的值：

`-其他属性 @{'AttributeLDAPDisplayName'=值}`

要为某个属性指定多个值：

`-其他属性 @{'AttributeLDAPDisplayName'=value1, value2, ...}`

您可以使用分号（;）来分隔多个属性，从而为这些属性指定值。以下语法展示了如何为多个属性设置值：

`-其他属性 @{'Attribute1LDAPDisplayName'=值; 'Attribute2LDAPDisplayName'=值1,值2;...}`

```yaml
Type: Hashtable
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

### -ProtectedFromAccidentalDeletion
指定是否阻止对象被删除。当此属性设置为 $True 时，不更改该属性的值就无法删除相应的对象。此参数的可接受值为：

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RedundantServerTopologyEnabled
该参数用于指示命令行工具（cmdlet）在发生故障之前是否会在站点之间创建多余的连接。当该参数被启用时，将禁用“知识一致性检查器”（Knowledge Consistency Checker，简称KCC）的故障转移功能。同时还需要禁用对失败连接的自动检测功能（需要设置 +IS_TOPL_DETECT_STALE_DISABLED）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReplicationSchedule
指定该站点内连接之间的默认复制计划（站点内复制）。

```yaml
Type: ActiveDirectorySchedule
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScheduleHashingEnabled
该参数用于指示 cmdlet 是否在整个计划间隔内随机分配复制开始时间，而不仅仅是该间隔的第一个季度。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务（AD DS）实例，为此请提供相应的域名或目录服务器对应的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（AD LDS）、AD DS 或 Active Directory 快照实例。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the AD DS Windows PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

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

### -TopologyCleanupEnabled
该选项用于指示 cmdlet 是否支持拓扑结构的清理。当该功能启用时，可以防止 KCC 删除那些不必要的连接对象。如果您希望自行负责删除多余的旧连接，请禁用此选项。另外，您也可以通过创建手动连接来控制或调整拓扑结构，这类连接不会被 KCC 自动删除。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TopologyDetectStaleEnabled
该选项用于指示某个 cmdlet 是否支持检测拓扑中的“失效”（即不再可用的）服务器。这样可以防止 Kerberos 密钥分配中心（KCC）将这些无法访问的服务器从拓扑中排除；也就是说，KCC 会使用备用服务器来重新路由复制请求。只有当网络通信非常不稳定且预计会出现短暂中断时，才应使用此选项。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TopologyMinimumHopsEnabled
该参数用于指示某个Cmdlet是否支持启用拓扑结构中的“最小跳数”（即数据传输过程中的最短路径）功能。当此功能被启用时，可以防止KCC（Knowledge Center Client）在站点内部的复制过程中生成不必要的优化连接。这些优化连接虽然能够降低复制延迟，但建议不要将其禁用，因为这可能会导致其他性能问题。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UniversalGroupCachingEnabled
该参数用于指示某个cmdlet是否支持通用组（universal groups）的缓存功能。如果此参数的值为“true”，则表示该站点会缓存通用组，这些通用组存储在全局目录（Global Catalog, GC）服务器上。对于那些本地没有GC服务器的站点来说，这一功能非常有用。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UniversalGroupCachingRefreshSite
当启用了通用组缓存功能时，该属性用于指定从中获取缓存的网站名称。

```yaml
Type: ADReplicationSite
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

### -WindowsServer2000BridgeheadSelectionMethodEnabled
实现了 Windows 2000 Server 中针对每个目录分区及传输方式选择单一桥头服务器的方法。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WindowsServer2000KCCISTGSelectionBehaviorEnabled
该属性用于指示某个Cmdlet是否实现了Windows 2000 Server中用于选择ISTG（Instance Storage Target Group）的方法。默认值为“Off”（关闭）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WindowsServer2003KCCBehaviorEnabled
实现了与 Windows Server 2003 林功能级别一致的 KCC（Kerberos Constrained Catalog）操作。如果站点中的所有域控制器都运行的是 Windows Server 2003，则可以设置此选项。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WindowsServer2003KCCIgnoreScheduleEnabled
该选项用于指示是否忽略计划（即是否不按照预定的时间表进行操作）。当系统运行在 Windows Server 2003 或 Windows Server 2003 Interim 版本，并且启用了森林功能级别设置时，KCC（知识库控制）会提供相应的控制机制，允许用户选择忽略计划。在这种情况下，数据复制仍会在指定的时间间隔内自动进行，并且始终能够保证数据的可用性。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WindowsServer2003KCCSiteLinkBridgingEnabled
该参数用于指示某个cmdlet是否支持站点链接桥接功能。当森林功能级别设置为Windows Server 2003或Windows Server 2003 Interim时，可以通过KCC（知识库一致性控制器）来控制是否启用或禁用站点链接桥接功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management_ADReplicationSite
通过 `Instance` 参数接收到一个站点对象，该站点对象是新站点对象的模板。

## 输出

### 无或 Microsoft.ActiveDirectory.Management_ADReplicationSite

## 备注

## 相关链接

[Get-ADReplicationSite](./Get-ADReplicationSite.md)

[ Remove-ADReplicationSite](./Remove-ADReplicationSite.md)

[Set-ADReplicationSite](./Set-ADReplicationSite.md)
