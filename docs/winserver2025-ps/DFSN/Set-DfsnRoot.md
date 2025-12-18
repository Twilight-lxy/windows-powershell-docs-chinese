---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespace.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/set-dfsnroot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsnRoot
---

# Set-DfsnRoot

## 摘要
更改DFS命名空间的设置。

## 语法

```
Set-DfsnRoot [-Path] <String> [[-EnableSiteCosting] <Boolean>] [[-EnableInsiteReferrals] <Boolean>]
 [[-EnableAccessBasedEnumeration] <Boolean>] [[-EnableRootScalability] <Boolean>]
 [[-EnableTargetFailback] <Boolean>] [[-Description] <String>] [[-State] <State>]
 [[-TimeToLiveSec] <UInt32>] [[-GrantAdminAccounts] <String[]>] [[-RevokeAdminAccounts] <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Set-DfsnRoot` cmdlet 用于更改分布式文件系统（DFS）命名空间的相关设置。

你可以使用此cmdlet来启用或禁用以下设置：

- **Site costing**
- **In-site referrals**
- **Access-based enumeration**
- **Root scalability**
- **Target failback**

You can also add or change a descriptive comment, change the state of the DFS namespace, or set the
Time to Live (TTL) interval for referrals.

To manage the DFS namespace, you can use this cmdlet to grant or revoke permissions to users or user
groups. Users who have these permissions can add, remove, and modify namespace folders and folder
targets for the DFS namespace.

For more information about DFS namespaces, see
[Overview of DFS Namespaces](https://technet.microsoft.com/library/cc730736) on TechNet.

## 示例

### Example 1: Change root scalability and TTL

```powershell
Set-DfsnRoot -Path '\\Contoso\AccountingResources' -EnableRootScalability $true -TimeToLiveSec 900
```

This command modifies settings for the DFS namespace that has the path
`\\Contoso\AccountingResources`. The command enables root scalability, which allows the DFS
namespace server to poll domain controllers for updates. The command also sets the referral TTL
interval to 900 seconds.

## 参数

### -AsJob

Runs the cmdlet as a background job. Use this parameter to run commands that take a long time to
complete.

The cmdlet immediately returns an object that represents the job and then displays the command
prompt. You can continue to work in the session while the job completes. To manage the job, use the
`*-Job` cmdlets. To get the job results, use the
[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet.

For more information about Windows PowerShell background jobs, see
[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251).

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

Runs the cmdlet in a remote session or on a remote computer. Enter a computer name or a session
object, such as the output of a [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)
or [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet. The default is the
current session on the local computer.

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

Prompts you for confirmation before running the cmdlet.

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

Specifies a description for a DFS namespace.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: desc

Required: False
Position: 6
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableAccessBasedEnumeration

Indicates whether a DFS namespace uses Access-based enumeration. If this value is `$true`, a DFS
namespace server shows a user only the files and folders that the user can access.

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: abe, abde

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableInsiteReferrals

该值用于指示DFS命名空间服务器是否仅向客户端提供与客户端位于同一站点内的引用（referrals）。如果值为 `$true`，则DFS命名空间服务器仅提供同站点的引用；如果值为 `$false`，则会先提供同站点的引用，然后再提供其他引用的信息。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: insite

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableRootScalability

该值表示DFS命名空间是否使用“根级可扩展性模式”（root scalability mode）。如果值为`$true`，则DFS命名空间服务器会定期连接到最近的域控制器以获取命名空间更新信息；如果值为`$false`，则服务器会连接到主域控制器（PDC）模拟器。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: RootScalability, rootscale

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableSiteCosting

该参数用于指示DFS命名空间是否使用基于成本的选择机制。当客户端无法访问某个文件夹目标时，DFS命名空间服务器会选择资源消耗最少的替代方案。如果您为该参数设置 `$true` 的值，DFS命名空间将优先选择高速连接，而非广域网（WAN）连接。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: SiteCosting, sitecost

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableTargetFailback

该值用于指示DFS命名空间是否使用目标服务器的故障切换功能。当客户端尝试访问服务器上的目标链接，但该服务器不可用时，客户端会自动切换到其他可用的服务器（即“引用”服务器）。如果此值为 `$true`，则一旦第一台服务器恢复正常可用性，客户端会重新切换回原来的目标服务器；如果此值为 `$false$`，则表示DFS命名空间服务器不要求客户端必须切换回首选的服务器。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: failback, TargetFailback

Required: False
Position: 5
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GrantAdminAccounts

指定一个账户数组。此 cmdlet 为 DFS 命名空间中指定的用户和用户组授予管理权限。这些用户可以添加、删除和修改命名空间文件夹及文件夹目标。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: GrantAdmin, GrantAdminAccess

Required: False
Position: 9
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path

指定一个用于DFS命名空间根目录的路径。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: RootPath, root, namespace, NamespaceRoot

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RevokeAdminAccounts

指定一个账户数组。此cmdlet会删除为DFS命名空间指定的用户和用户组的管理权限。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: RevokeAdmin, RevokeAdminAccess

Required: False
Position: 10
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -State

指定DFS命名空间根的状态。该参数的可接受值为：

- `Online`
- `Offline`

Clients do not receive referrals for a DFS namespace folder that is offline. If you set a namespace
root to a value of `Offline`, the entire namespace becomes inaccessible.

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.DfsNamespaceRootTarget.State
Parameter Sets: (All)
Aliases:
Accepted values: Offline, Online

Required: False
Position: 7
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不影响整个会话或计算机本身。

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

指定引用（referrals）的TTL间隔时间（以秒为单位）。客户端会将引用信息存储到根目标（root target）处，存储时间为指定的时长。根引用的默认TTL间隔为300秒。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: ttl, TimeToLive

Required: False
Position: 8
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet运行会发生的结果。但实际上这个cmdlet并没有被执行。

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

### System Boolean

### Microsoft.PowerShell Cmdletization GeneratedTypes.DfsNamespace.State

### System.UInt32

### System.String[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[Get-DfsnRoot](./Get-DfsnRoot.md)

[New-DfsnRoot](./New-DfsnRoot.md)

[Remove-DfsnRoot](./Remove-DfsnRoot.md)
