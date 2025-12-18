---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 07/01/2024
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/add-cauclusterrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-CauClusterRole
---

# Add-CauClusterRole

## 摘要
为指定的集群添加CAU（Clustered Authentication Unit）集群角色，该角色提供了自更新功能。

## 语法

### MonthlyDayOfWeek（默认值）

```
Add-CauClusterRole [-VirtualComputerObjectName <String>] [-GroupName <String>]
 [-StartDate <DateTime>] [-DaysOfWeek <Weekdays>] [-WeeksOfMonth <Int32[]>]
 [-CauPluginName <String[]>] [-CauPluginArguments <Hashtable[]>] [-MaxFailedNodes <Int32>]
 [-MaxRetriesPerNode <Int32>] [-NodeOrder <String[]>] [-PreUpdateScript <String>]
 [-PostUpdateScript <String>] [-ConfigurationName <String>] [-RequireAllNodesOnline]
 [-WarnAfter <TimeSpan>] [-StopAfter <TimeSpan>] [-RebootTimeoutMinutes <Int32>]
 [-SeparateReboots] [-RunPluginsSerially] [-StopOnPluginFailure] [-EnableFirewallRules]
 [-FailbackMode <FailbackType>] [-SuspendClusterNodeTimeoutMinutes <Int32>]
 [-SuspendRetriesPerNode <Int32>] [-WaitForStorageRepairTimeoutMinutes <Int32>] [-ForcePauseNoDrain]
 [-ForcePauseAndDrain] [-ForcePauseDrainAndReboot] [-SkipUpdateChecks]
 [-SiteAwareUpdatingOrder <String[]>] [-OsRollingUpgrade] [-AttemptSoftReboot]
 [-RebootMode <RebootType>] [[-ClusterName] <String>] [[-Credential] <PSCredential>] [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 每周

```
Add-CauClusterRole [-VirtualComputerObjectName <String>] [-GroupName <String>]
 [-StartDate <DateTime>] [-DaysOfWeek <Weekdays>] [-IntervalWeeks <Int32>]
 [-CauPluginName <String[]>] [-CauPluginArguments <Hashtable[]>] [-MaxFailedNodes <Int32>]
 [-MaxRetriesPerNode <Int32>] [-NodeOrder <String[]>] [-PreUpdateScript <String>]
 [-PostUpdateScript <String>] [-ConfigurationName <String>] [-RequireAllNodesOnline]
 [-WarnAfter <TimeSpan>] [-StopAfter <TimeSpan>] [-RebootTimeoutMinutes <Int32>] [-SeparateReboots]
 [-RunPluginsSerially] [-StopOnPluginFailure] [-EnableFirewallRules] [-FailbackMode <FailbackType>]
 [-SuspendClusterNodeTimeoutMinutes <Int32>] [-SuspendRetriesPerNode <Int32>]
 [-WaitForStorageRepairTimeoutMinutes <Int32>] [-ForcePauseNoDrain] [-ForcePauseAndDrain]
 [-ForcePauseDrainAndReboot] [-SkipUpdateChecks] [-SiteAwareUpdatingOrder <String[]>]
 [-OsRollingUpgrade] [-AttemptSoftReboot] [-RebootMode <RebootType>] [[-ClusterName] <String>]
 [[-Credential] <PSCredential>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 有一次

```
Add-CauClusterRole [-VirtualComputerObjectName <String>] [-GroupName <String>] [-RunOnce]
 [-CauPluginName <String[]>] [-CauPluginArguments <Hashtable[]>] [-MaxFailedNodes <Int32>]
 [-MaxRetriesPerNode <Int32>] [-NodeOrder <String[]>] [-PreUpdateScript <String>]
 [-PostUpdateScript <String>] [-ConfigurationName <String>] [-RequireAllNodesOnline]
 [-WarnAfter <TimeSpan>] [-StopAfter <TimeSpan>] [-RebootTimeoutMinutes <Int32>] [-SeparateReboots]
 [-RunPluginsSerially] [-StopOnPluginFailure] [-EnableFirewallRules] [-FailbackMode <FailbackType>]
 [-SuspendClusterNodeTimeoutMinutes <Int32>] [-SuspendRetriesPerNode <Int32>]
 [-WaitForStorageRepairTimeoutMinutes <Int32>] [-ForcePauseNoDrain] [-ForcePauseAndDrain]
 [-ForcePauseDrainAndReboot] [-SkipUpdateChecks] [-SiteAwareUpdatingOrder <String[]>]
 [-OsRollingUpgrade] [-AttemptSoftReboot] [-RebootMode <RebootType>] [[-ClusterName] <String>]
 [[-Credential] <PSCredential>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Add-CauClusterRole` cmdlet 用于向指定的集群添加“Cluster-Aware Updating (CAU)”集群角色，该角色可为集群提供自动更新的功能。一旦 CAU 集群角色被添加到集群中，故障转移集群就可以按照用户设定的时间表自行进行更新，而无需外部计算机来协调更新过程。

要运行此cmdlet，必须在每个节点上启用Windows PowerShell远程功能。为此，请运行`Enable-PSRemoting` cmdlet。此外，请确保在每个节点上也启用了**Windows远程管理 - 兼容模式（HTTP-In）**防火墙例外规则。

## 示例

### 示例 1：在指定的集群上以特定的间隔添加一个 CAU 集群角色

```powershell
$parameters = @{
    ClusterName = 'CONTOSO-FC1'
    DaysOfWeek = 'Tuesday',
                    'Saturday'
    WeeksOfMonth = '2',
                    '4'
    MaxFailedNodes = '2'
    MaxRetriesPerNode = '2'
    PostUpdateScript = '\\CONTOSOFileShare\scripts\verifyupdatesinstalled.ps1'
    RequireAllNodesOnline = $true
    EnableFirewallRules = $true
    Force = $true
}
Add-CauClusterRole @parameters
```

此命令会在名为 **CONTOSO-FC1** 的集群上添加一个名为 “CAU Clustered Role” 的角色（使用默认名称）。该角色的配置为：在每月的第二个和第四周的周二及周六执行更新操作。在执行更新操作时，每个节点的最大故障次数为 2 次，每个节点的最大重试次数也为 2 次。在每个节点完成更新后，会运行一个名为 `verifyupdatesinstalled.ps1` 的脚本。在开始更新操作之前，该集群的所有节点都必须处于运行状态。如果尚未启用相关设置，则会在每个集群节点上启用 “Remote Shutdown Windows Firewall” 规则组。由于该命令使用了 **Force** 参数，因此执行此 cmdlet 时不会显示确认提示。

这个例子使用了“拆分”（splatting）技术，将 `$parameters` 变量中的参数值传递给命令。有关 [拆分](/powershell/module/microsoft.powershell.core/about/about_splatting) 的更多信息，请参阅相关文档。

### 示例 2：在指定的集群上以特定的时间间隔添加一个 CAU 集群角色

```powershell
$parameters = @{
    ClusterName = 'CONTOSO-FC1'
    DaysOfWeek = 'Tuesday',
                    'Saturday'
    IntervalWeeks = '3'
    MaxFailedNodes = '2'
    MaxRetriesPerNode = '2'
    EnableFirewallRules = $true
    Force = $true
}
Add-CauClusterRole @parameters
```

该命令在名为 **CONTOSO-FC1** 的集群上添加了一个名为 “CAU Clustered Role” 的角色（使用默认名称）。此角色的配置是：每周二和周六执行更新操作，更新间隔为三周。在一次更新操作中，允许失败的节点数量最多为两个，每个节点的重试次数最多为两次。即使集群中的所有节点并未运行（只要集群本身具有法定人数并处于运行状态），更新操作也可以开始。如果尚未启用相关设置，则会在每个集群节点上启用 “Remote Shutdown Windows Firewall” 规则组。由于该命令使用了 **Force** 参数，因此执行此 cmdlet 时不会显示确认提示。

这个例子使用了“拆分”（splatting）技术，将 `$parameters` 变量中的参数值传递给命令。有关 [拆分](/powershell/module/microsoft.powershell.core/about/about_splatting) 的更多信息，请参阅相关文档。

### 示例 3：使用插件在指定的集群上添加一个 CAU 集群角色

```powershell
$parameters = @{
    ClusterName = 'CONTOSO-FC1'
    CauPluginName = 'Microsoft.WindowsUpdatePlugin',
                    'Microsoft.HotfixPlugin'
    CauPluginArguments = @{'IncludeRecommendedUpdates' = 'True'},
                         @{'HotfixRootFolderPath' = '\\CauHotfixSrv\shareName'}
    StopOnPluginFailure = $true
    EnableFirewallRules = $true
    Force = $true
}
Add-CauClusterRole @parameters
```

此命令会在名为 **CONTOSO-FC1** 的集群上添加一个名为 CAU 的集群角色（使用默认名称）。该 CAU 集群角色被配置为使用 **Microsoft.WindowsUpdatePlugin** 插件来执行更新操作，同时将可选参数 **IncludeRecommendedUpdates** 设置为 `True`；此外，它还使用 **Microsoft.HotfixPlugin** 插件，并指定 hotfix 文件的存储路径为 `\\CauHotfixSrv\shareName`，并采用默认的热fix 配置文件。如果在某个节点上使用 **Microsoft.WindowsUpdatePlugin** 安装更新时发生故障，系统会转而使用 **Microsoft.HotfixPlugin** 来完成更新过程。如果尚未启用相关设置，则会在每个集群节点上启用 “Remote Shutdown Windows Firewall” 规则组。由于该命令使用了 **Force** 参数，因此执行过程中不会显示确认提示信息。

这个例子使用了“拆分”（splatting）技术，将 `$parameters` 变量中的参数值传递给命令。有关 [拆分](/powershell/module/microsoft.powershell.core/about/about_splatting) 的更多信息，请参阅相关文档。

## 参数

### -AttemptSoftReboot

表示CAU集群角色尝试对故障转移集群执行内核软重启（KSR）操作。

KSR 可以绕过 BIOS/固件的初始化过程。只有那些不需要进行 BIOS/固件初始化的更新才能使用 KSR 来完成。

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

### -CauPluginArguments

为每个需要更新的插件指定一组名称=值的对作为参数供其使用。

例如，要为一个插件指定一个“Domain”参数：

- `@{Domain=Domain.local}`

你可以用分号（;）分隔在一组中的多对内容。例如：

- `@{name1=value1;name2=value2;name3=value3}`

These name=value pairs must be meaningful to the **CauPluginName** parameter that you specify. If
you specify arguments for more than one plug-in, provide the sets of name=value pairs in the order
that you pass values in **CauPluginName**, separated by commas. For instance:

- `@{name1=value1;name2=value2;name3=value3},@{name4=value4;name5=value5}`

对于默认的 **Microsoft.WindowsUpdatePlugin** 插件来说，不需要任何参数。以下参数是可选的：

- **'IncludeRecommendedUpdates'='\<Value\>'**: Boolean value to indicate that recommended updates
  will be applied in addition to important updates on each node. If not specified, the default value
  is False.
- A standard Windows Update Agent query string that specifies criteria used by the Windows Update
  Agent to filter the updates that will be applied to each node. For a name, use **QueryString** and
  for a value, enclose the full query in quotation marks. If not specified, then the
  **Microsoft.WindowsUpdatePlugin** plug-in by default uses the following argument:
- `QueryString="IsInstalled=0 and Type='Software' and IsHidden=0 and IsAssigned=1"`

有关默认的 **Microsoft.WindowsUpdatePlugin** 插件的查询字符串以及可以包含在查询字符串中的标准（如 IsInstalled）的更多信息，请参阅 [IUpdateSearcher::Search 方法](/windows/win32/api/wuapi/nf-wuapi-iupdatesearcher-search)。

对于 `Microsoft.HotfixPlugin` 插件，需要以下参数：

- **HotfixRootFolderPath=\<Path\>**: The UNC path to a hotfix root folder in an SMB share with a
  structure that contains the updates to apply and that contains the hotfix configuration file.

以下参数对于 **Microsoft.HotfixPlugin** 插件来说是可选的：

- **RequireSmbEncryption=\<Value\>**: Boolean value to indicate that SMB Encryption will be enforced
  for accessing data from the SMB share. If not specified, the default value is False. To ensure the
  integrity of the data accessed from the SMB share, the plug-in requires that the share is enabled
  for either SMB signing or SMB Encryption.
- **DisableAclChecks=\<Value\>**: Boolean value to indicate that the plug-in will check for
  sufficient permissions on the hotfix root folder and the hotfix configuration file. If not
  specified, the default value is False.
- **HotfixInstallerTimeoutMinutes=\<Integer\>**: The length of time in minutes that the plug-in
  allows the hotfix installer process to return. If not specified, the default value is 30 minutes.
- **HotfixConfigFileName=\<name\>**: Name for the hotfix configuration file. If not specified, the
  default name `DefaultHotfixConfig.xml` is used. For more information about required and optional
  arguments for the **Microsoft.HotfixPlugin** plug-in, see
  [How Cluster-Aware Updating plug-ins work](/windows-server/failover-clustering/cluster-aware-updating-plug-ins).

```yaml
Type: Hashtable[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CauPluginName

指定在执行扫描或更新时使用的一个或多个插件。您可以输入多个值，这些值之间用逗号分隔。默认使用的插件是 **Microsoft.WindowsUpdatePlugin**。该插件负责协调每个集群节点上运行的 Windows Update Agent 软件；该软件在从 Windows Update、Microsoft Update 或 Windows Server Update Services (WSUS) 服务器下载更新时也会被使用。有关插件如何与 Cluster-Aware Updating (CAU) 集成的更多信息，请参阅 [Cluster-Aware Updating 插件的工作原理](/windows-server/failover-clustering/cluster-aware-updating-plug-ins)。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClusterName

指定用于创建 CAU 集群角色的集群名称。此参数仅在以下情况下才需要：要么不在故障转移集群节点上运行该 cmdlet，要么使用该 cmdlet 引用与执行命令的地点不同的故障转移集群。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ConfigurationName

指定 Windows PowerShell 会话配置，该配置定义了用于运行由 **PreUpdateScript** 和 **PostUpdateScript** 参数指定的脚本以及 cmdlet 的会话，并可以限制可运行的 cmdlet 的范围。如果指定了更新前或更新后的脚本，但没有指定相应的配置名称，则将使用 Windows PowerShell 内置的默认会话配置。

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

### -Credential

指定目标集群的管理凭据。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DaysOfWeek

指定更新任务将被触发的星期几。可以指定多个值，这些值可以用逗号分隔，或者以十六进制数之和的形式表示。

该参数的可接受值包括：

- **Sunday:** (0x01)
- **Monday:** (0x02)
- **Tuesday:** (0x04)
- **Wednesday:** (0x08)
- **Thursday:** (0x10)
- **Friday:** (0x20)
- **Saturday:** (0x40)

```yaml
Type: Weekdays
Parameter Sets: MonthlyDayOfWeek, Weekly
Aliases:
Accepted values: None, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableFirewallRules

该 cmdlet 用于在每个集群节点上启用 Windows 防火墙的 “Remote Shutdown” 规则组（如果该规则组尚未被启用的话）。如果指定了 `EnableFirewallRules` 参数，那么每当 CAU 集群角色执行更新操作时，CAU 也会自动重新启用 “Remote Shutdown” 规则组——以防在此期间有人手动禁用了这些规则。

启用此规则组后，在每次更新过程中，每个集群节点都将允许接收外部通信；这样一来，CAU（Cloud Automation Unit）就可以远程关闭并重新启动相应的节点（如果更新安装需要重启的话）。如果在集群节点上使用了Windows防火墙且未启用该规则组，更新过程将会失败。需要注意的是，“Remote Shutdown Windows Firewall”规则组本身是无法被启用的——因为它会与为Windows防火墙配置的组策略设置发生冲突。

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

### -FailbackMode

指定在更新节点结束后用于将已迁移的工作负载重新恢复到该节点上的方法。所谓“已迁移的工作负载”，是指那些之前运行在该节点上，但后来被转移到另一个节点上的工作负载。

该参数的可接受值包括：

- `NoFailback`
- `Immediate`
- `Policy`

The default value is **Immediate**.

```yaml
Type: FailbackType
Parameter Sets: (All)
Aliases:
Accepted values: NoFailback, Immediate, Policy

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令执行，而不会要求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: f

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForcePauseAndDrain

表示 CAU 集群角色会强制集群节点暂停运行，并释放相关角色（即让这些节点不再承担特定的功能或任务）。

强制排水机制会将该组的角色从负责排水的节点上移除，即使该组本身无法进行移动。某个组可能无法移动的原因在于没有其他节点能够容纳它，或者该组被锁定了。

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

### -ForcePauseDrainAndReboot

表示CAU集群角色会强制集群节点暂停运行、释放当前承担的角色，并重新启动节点。

强制排水机制会将该组的角色从负责排水的节点上移除，即使该组本身无法进行移动。某个组可能无法移动的原因在于没有其他节点能够容纳它，或者该组被锁定了。

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

### -ForcePauseNoDrain

表示“CAU集群角色”强制集群节点暂停运行。这些节点的数据并不会被清除（即节点上的数据不会被删除）。

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

### -GroupName

指定用于 CAU 集群角色的资源组的 NetBIOS 名称。

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

### -IntervalWeeks

用于指定任务触发之间的时间间隔（以周为单位）。当间隔值为 1 时，任务将按每周的频率执行；当间隔值为 2 时，任务将每隔一周执行一次。

```yaml
Type: Int32
Parameter Sets: Weekly
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxFailedNodes

指定更新过程中最多可以出现故障的节点数量。如果超过这个数量的节点发生故障，那么更新操作将会停止。该数值的范围是 0 到 1（小于集群中的实际节点数）。对于大多数集群来说，默认值为节点总数的大约三分之一。

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

### -MaxRetriesPerNode

指定更新过程尝试运行的最大次数。这包括任何更新前和更新后的脚本。更新过程会针对每个节点进行重试。最大值为 64，默认值为 3。

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

### -NodeOrder

指定一个集群节点名称数组，并按照这些节点应被更新的顺序排列它们。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OsRollingUpgrade

表示CAU集群角色可以在不中断Hyper-V或Scale-Out文件服务器工作负载的情况下，升级集群节点的操作系统。

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

### -PostUpdateScript

指定一个 Windows PowerShell 脚本的路径和文件名，该脚本将在更新完成后、以及节点退出维护模式后立即在每个节点上运行。文件的扩展名必须是 `.ps1`，并且路径与文件名的总长度不得超过 260 个字符。作为最佳实践，该脚本应存储在集群存储的磁盘上或高可用性的网络共享位置，以确保所有集群节点都能访问该脚本。

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

### -PreUpdateScript

指定一个 Windows PowerShell 脚本的路径和文件名，该脚本将在更新开始之前以及节点进入维护模式之前在每个节点上运行。文件的扩展名必须是 `.ps1`，并且路径长度加上文件名的总长度不得超过 260 个字符。作为最佳实践，该脚本应位于集群存储中的磁盘上或高可用性的网络共享位置，以确保所有集群节点都能访问该脚本。如果预更新脚本失败，则该节点将不会被更新。

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

### -RebootMode

指定在更新过程中对集群中的每个节点使用哪种类型的重启方式。可选的值包括：

- `ClusProp`
- `FullReboot`
- `SoftReboot`
- `PluginCustomReboot`
- `OrchestratorDefault`

```yaml
Type: RebootType
Parameter Sets: (All)
Aliases:
Accepted values: ClusProp, FullReboot, SoftReboot, PluginCustomReboot, OrchestratorDefault

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RebootTimeoutMinutes

指定CAU允许节点重启的时间（以分钟为单位）。如果节点重启未能在这段时间内完成，那么在该节点上执行的更新操作将被标记为失败。

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

### -RequireAllNodesOnline

表示该cmdlet在开始更新之前会确保所有集群节点都处于在线状态且可被访问。

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

### -RunOnce

指定 CAU 运行应仅执行一次，而不是按照定期计划进行。如果您只需要对集群节点进行一次性更新，这种方法会非常有用。

```yaml
Type: SwitchParameter
Parameter Sets: Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RunPluginsSerially

当你在更新过程中使用 **CauPluginName** 参数时，该 cmdlet 会扫描每个集群节点以查找适用的更新，并按照插件使用的顺序对这些更新进行分阶段处理（即依次为每个插件安装相应的更新）。默认情况下，CAU 会并行扫描并分阶段处理所有插件所需的更新。无论此参数的配置如何，CAU 仍会按顺序为每个插件安装相应的更新。

该参数仅在**CauPluginName**参数中指定了多个插件时才有效。如果只指定了一个插件，系统会显示警告提示。

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

### -SeparateReboots

该命令表示：在每个插件完成对节点的更新安装后（如果某个插件的更新需要重新启动节点），此命令会关闭相关组件（CAU），然后重启该集群节点。默认情况下，在更新过程中，所有插件都会先完成对节点的更新安装，之后节点才会进行一次重启。

该参数仅在**CauPluginName**参数中指定了多个插件时才有效。如果只指定了一个插件，系统会显示警告提示。

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

### -SiteAwareUpdatingOrder

指定CAU集群角色更新集群节点的顺序。

默认情况下，CAU会根据节点的活动程度来决定更新节点的顺序。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipUpdateChecks

表示CAU集群角色会跳过更新检查步骤。

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

### -StartDate

指定了可以触发更新运行的最早日期。

```yaml
Type: DateTime
Parameter Sets: MonthlyDayOfWeek, Weekly
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StopAfter

指定在更新任务未完成的情况下，取消该任务的延迟时间（以分钟为单位）。这个时间间隔可以使用 Windows PowerShell 中提供的标准格式来表示，例如 `01:30:00` 表示一小时三十分钟。默认情况下，更新任务有无限的时间来完成。

如果指定了更新前的脚本或更新后的脚本，那么运行这些脚本并完成更新的所有过程必须在规定的时间限制内完成。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StopOnPluginFailure

该参数表示：当插件被停止时，此 cmdlet 会协调后续对该节点的更新操作。如果在更新过程中使用了多个插件，默认情况下，某个插件的故障不会影响其他插件对节点的更新操作。该参数仅在 **CauPluginName** 参数中指定了多个插件时才有效；如果只指定了一个插件，则会显示警告信息。

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

### -SuspendClusterNodeTimeoutMinutes

如果底层的集群环境处于降级状态，该参数指定了CAU（Cluster Autonomization Unit）应等待`Suspend-ClusterNode` cmdlet成功执行的最大时间长度。

如果 `Suspend-ClusterNode` 命令因 “ERROR_CLUSTER_SPACE_DEGRADED” 错误而失败，CAU 会继续重试，直到达到 `SuspendClusterNodeTimeoutMinutes` 所设定的时间限制；如果该命令最终成功执行，则重试操作将终止。这些由于 “ERROR_cluster_space_DEGRADED” 错误导致的重试次数不会计入用户设置的 `MaxRetriesPerNode` 参数所规定的总重试次数限制中。

超时值是针对每个集群节点设置的。因此，在最坏的情况下，CAU 可能会为集群中的每个节点花费该超时值所指定的时间。

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

### -SuspendRetriesPerNode

指定在尝试暂停某个节点后重试的次数，之后才会继续处理下一个节点。

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

### -VirtualComputerObjectName

指定一个预先准备好的虚拟计算机对象的名称，该对象将被 CAU 集群角色使用。有关更多信息，请参阅 [预准备集群名称帐户的步骤](/windows-server/failover-clustering/configure-ad-accounts#steps-for-prestaging-the-cluster-name-account)。如果未指定名称，则会使用自动生成的名称来创建虚拟计算机对象。自动生成名称的前提是集群名称对象具有在 Active Directory 中创建该虚拟计算机对象的权限。

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

### -WaitForStorageRepairTimeoutMinutes

指定在继续更新之前，需要等待存储系统在节点上完成修复的时间（以分钟为单位）。

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

### -WarnAfter

指定在更新运行（包括任何更新前和更新后的脚本）未完成之后，需要经过多少分钟才会记录警告信息。默认情况下，无论更新运行花费了多长时间，都不会记录任何警告信息。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WeeksOfMonth

指定每月应运行更新任务的周数。数值 5 表示该月的最后一周。

```yaml
Type: Int32[]
Parameter Sets: MonthlyDayOfWeek
Aliases:

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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Disable-CauClusterRole](disable-cauclusterrole.md)

[Enable-CauClusterRole](enable-cauclusterrole.md)

[Get-CauClusterRole](get-cauclusterrole.md)

[Remove-CauClusterRole](remove-cauclusterrole.md)

[Set-CauClusterRole](set-cauclusterrole.md)
