---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespace.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/new-dfsnroot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-DfsnRoot
---

# New-DfsnRoot

## 摘要
创建一个深度优先搜索（DFS）命名空间。

## 语法

```
New-DfsnRoot [-Path <String>] [-TargetPath] <String> [-Type] <Type> [[-EnableSiteCosting] <Boolean>]
 [[-EnableInsiteReferrals] <Boolean>] [[-EnableAccessBasedEnumeration] <Boolean>]
 [[-EnableRootScalability] <Boolean>] [[-EnableTargetFailback] <Boolean>] [[-Description] <String>]
 [[-State] <State>] [[-TimeToLiveSec] <UInt32>] [[-GrantAdminAccounts] <String[]>] [[-TargetState] <State>]
 [[-ReferralPriorityClass] <ReferralPriorityClass>] [[-ReferralPriorityRank] <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`New-DfsnRoot` cmdlet 用于创建一个分布式文件系统（DFS）命名空间。你需要指定新命名空间的根路径和目标路径，并且还需要指定命名空间的类型：独立命名空间、Windows 2000 Server 模式（域版本 1）命名空间，或者 Windows Server 2008 模式（域版本 2）命名空间。

您可以为新命名空间指定相关设置。您可以使用此 cmdlet 来启用或禁用以下设置：

- Site costing.
- In-site referrals.
- Access-based enumeration.
- Root scalability.
- Target failback.

您还可以添加描述性注释，选择DFS命名空间和DFS根目标的状态，并设置引用请求的生存时间（TTL）间隔。

要管理DFS命名空间，您可以授予用户或用户组相应的权限。拥有这些权限的用户可以添加、删除和修改DFS命名空间中的文件夹及其目标对象。

有关DFS命名空间的更多信息，请参阅TechNet上的[DFS命名空间概述](https://technet.microsoft.com/library/cc730736)。

## 示例

### 示例 1：创建一个 Windows Server 2008 模式的域 DFS 命名空间

```powershell
New-DfsnRoot -TargetPath '\\Contoso-FS\AccountingResources' -Type 'DomainV2' -Path '\\Contoso\AccountingResources'
```

此命令创建一个DFS命名空间，其根目录位于路径`\\Contoso\AccountingResources`。该路径的根目标目录是共享文件夹`\\Contoso-FS\AccountingResources`。命名空间的类型为Windows Server 2008模式，具体类型被指定为`DomainV2`。

### 示例 2：创建一个独立的 DFS 命名空间

```powershell
New-DfsnRoot -TargetPath '\\Contoso-FS\Software' -Type 'Standalone' -EnableSiteCosting -Path '\\Contoso\Software'
```

此命令创建了一个独立的DFS命名空间，其根目录位于路径`\\Contoso\Software`，并且该命名空间的根目标指向`\\Contoso-FS\Software`。这个命名空间采用基于成本的站点选择机制来进行资源分配。

## 参数

### -AsJob

将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中执行其他操作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: Microsoft.Management.Infrastructure.CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

在运行cmdlet之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Description

为DFS命名空间指定一个描述。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: desc

Required: False
Position: 7
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableAccessBasedEnumeration

该属性用于指示一个DFS命名空间是否使用基于访问权限的文件枚举机制。如果值为`$true`，则DFS命名空间服务器仅向用户显示其有权访问的文件和文件夹。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: abe, abde

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableInsiteReferrals

该值用于指示DFS命名空间服务器是否仅向客户端提供位于同一站点内的引用（referrals）。如果该值为`$true`，则表示DFS命名空间服务器仅提供同一站点内的引用；如果该值为`$false`，则表示DFS命名空间服务器会先提供同一站点内的引用，然后再提供其他站点的引用。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: insite

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableRootScalability

该值用于指示DFS命名空间是否使用“根级可扩展性模式”（root scalability mode）。如果值为`$true`，则DFS命名空间服务器会定期连接到最近的域控制器以获取命名空间更新信息；如果值为`$false`，则服务器会连接到主域控制器（PDC）仿真器。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: RootScalability, rootscale

Required: False
Position: 5
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableSiteCosting

该参数用于指示DFS命名空间是否采用基于成本的选择机制。当客户端无法在本地访问某个文件夹目标时，DFS命名空间服务器会选择资源消耗最少的替代方案。如果您为该参数设置 `$true` 的值，DFS命名空间将优先使用高速链接（而非广域网（WAN）链接）。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: SiteCosting, sitecost

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableTargetFailback

该值用于指示DFS命名空间是否使用目标服务器的故障恢复（failback）机制。当客户端尝试访问某台服务器上的目标资源，而该服务器不可用时，客户端会自动切换到另一台可用的服务器。如果该值为`$true`，则一旦第一台服务器恢复正常可用性，客户端会重新连接至原来的目标服务器；如果该值为`$false`，则表示DFS命名空间服务器不会强制客户端切换回首选的服务器。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: failback, TargetFailback

Required: False
Position: 6
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GrantAdminAccounts

指定一个账户数组。此cmdlet为指定的用户和用户组授予DFS命名空间的管理权限。这些用户可以添加、删除和修改命名空间文件夹及文件夹目标。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: GrantAdmin, GrantAdminAccess

Required: False
Position: 10
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path

指定一个DFS命名空间根目录的路径。该路径必须是唯一的，并且不能是与现有DFS命名空间相同的名称。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: RootPath, root, namespace, NamespaceRoot

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReferralPriorityClass

用于指定DFS命名空间根节点的目标优先级类别。目标优先级允许你对站点内的目标进行分类和排序：你可以指定某些目标获得最高或最低的优先级，并根据这些目标的连接成本来决定DFS客户端应选择哪些目标进行连接。该参数的可接受取值为：

- `GlobalHigh` - The highest priority class for a DFS target. Targets assigned this class receive
  global preference.
- `SiteCostHigh` - The highest site cost priority class for a DFS target. Targets assigned this
  class receive the most preference among targets of the same site cost for a given DFS client.
- `SiteCostNormal` - The middle or normal site cost priority class for a DFS target.
- `SiteCostLow` - The lowest site cost priority class for a DFS target. Targets assigned this class
  receive the least preference among targets of the same site cost for a given DFS client.
- `GlobalLow` - The lowest level of priority class for a DFS target. Targets assigned this class
  receive the least preference globally.

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.DfsNamespaceRootTarget.ReferralPriorityClass
Parameter Sets: (All)
Aliases: PriorityClass, Class
Accepted values: SiteCostNormal, GlobalHigh, SiteCostHigh, SiteCostLow, GlobalLow

Required: False
Position: 12
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReferralPriorityRank

用于指定DFS命名空间中根目标的优先级等级（以整数表示）。数值越小，优先级越高；数值为零（0）表示最高优先级。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: PriorityRank, Rank

Required: False
Position: 13
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -State

指定DFS命名空间根的状态。该参数的可接受值包括：

- `Online`
- `Offline`

Clients do not receive referrals for a DFS namespace folder that is offline. If you set a namespace
root to a value of Offline, the entire namespace becomes inaccessible.

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.DfsNamespaceRootTarget.State
Parameter Sets: (All)
Aliases:
Accepted values: Offline, Online

Required: False
Position: 8
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetPath

Specifies a path for a root target of the DFS namespace.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: NamespaceRootTarget

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetState

Specifies the state of the DFS namespace root target. The acceptable values for this parameter are:

- `Online`
- `Offline`

Clients do not receive referrals for a DFS namespace folder target that is Offline.

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.DfsNamespaceRootTarget.State
Parameter Sets: (All)
Aliases:
Accepted values: Offline, Online

Required: False
Position: 11
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的cmdlet的最大数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。该限制仅适用于当前执行的cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TimeToLiveSec

指定引用的TTL间隔（以秒为单位）。客户端会将引用信息存储到根目标对象上，存储时间为该TTL间隔所指定的时长。根引用的默认TTL间隔为300秒。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: ttl, TimeToLive

Required: False
Position: 9
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Type

将DFS命名空间的类型指定为一个Type对象。此参数的可接受值包括：

- `Standalone` - Specifies a stand-alone namespace.
- `DomainV1` - Specifies a Windows 2000 Server mode domain namespace.
- `DomainV2` - Specifies a Windows Server 2008 mode domain namespace.

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.DfsNamespace.Type
Parameter Sets: (All)
Aliases:
Accepted values: Standalone, DomainV1, DomainV2

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.PowerShell Cmdletization GeneratedTypes.DfsNamespace.Type

### System(Boolean)

### Microsoft.PowerShell Cmdletization GeneratedTypes.DfsNamespace.State

### System.UInt32

### System.String[]

### Microsoft.PowerShell Cmdletization GeneratedTypes.DfsNamespaceRootTarget.State

### Microsoft.PowerShell CmdletizationGeneratedTypes.DfsNamespaceRootTarget.ReferralPriorityClass

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[Get-DfsnRoot](./Get-DfsnRoot.md)

[Remove-DfsnRoot](./Remove-DfsnRoot.md)

[Set-DfsnRoot](./Set-DfsnRoot.md)
