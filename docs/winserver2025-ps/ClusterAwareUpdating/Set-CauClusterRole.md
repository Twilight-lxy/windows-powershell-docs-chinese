---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 07/01/2024
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/set-cauclusterrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-CauClusterRole
---

# 设置 CauClusterRole

## 摘要
为指定集群上的 CAU 集群角色设置配置属性。

## 语法

### MonthlyDayOfWeek（默认值）

```
Set-CauClusterRole [-UseDefault] [-StartDate <DateTime>] [-DaysOfWeek <Weekdays>]
 [-WeeksOfMonth <Int32[]>] [-CauPluginName <String[]>] [-CauPluginArguments <Hashtable[]>]
 [-MaxFailedNodes <Int32>] [-MaxRetriesPerNode <Int32>] [-NodeOrder <String[]>]
 [-PreUpdateScript <String>] [-PostUpdateScript <String>] [-ConfigurationName <String>]
 [-RequireAllNodesOnline] [-WarnAfter <TimeSpan>] [-StopAfter <TimeSpan>]
 [-RebootTimeoutMinutes <Int32>] [-SeparateReboots] [-RunPluginsSerially] [-StopOnPluginFailure]
 [-EnableFirewallRules] [-FailbackMode <FailbackType>] [-SuspendClusterNodeTimeoutMinutes <Int32>]
 [-SuspendRetriesPerNode <Int32>] [-WaitForStorageRepairTimeoutMinutes <Int32>] [-ForcePauseNoDrain]
 [-ForcePauseAndDrain] [-ForcePauseDrainAndReboot] [-SkipUpdateChecks]
 [-SiteAwareUpdatingOrder <String[]>] [-OsRollingUpgrade] [-AttemptSoftReboot]
 [-RebootMode <RebootType>] [[-ClusterName] <String>] [[-Credential] <PSCredential>] [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 立即更新

```
Set-CauClusterRole [-UpdateNow] [[-ClusterName] <String>] [[-Credential] <PSCredential>] [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### UseDefault

```
Set-CauClusterRole [-UseDefault] [[-ClusterName] <String>] [[-Credential] <PSCredential>] [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 每周

```
Set-CauClusterRole [-UseDefault] [-StartDate <DateTime>] [-DaysOfWeek <Weekdays>]
 [-IntervalWeeks <Int32>] [-CauPluginName <String[]>] [-CauPluginArguments <Hashtable[]>]
 [-MaxFailedNodes <Int32>] [-MaxRetriesPerNode <Int32>] [-NodeOrder <String[]>]
 [-PreUpdateScript <String>] [-PostUpdateScript <String>] [-ConfigurationName <String>]
 [-RequireAllNodesOnline] [-WarnAfter <TimeSpan>] [-StopAfter <TimeSpan>]
 [-RebootTimeoutMinutes <Int32>] [-SeparateReboots] [-RunPluginsSerially] [-StopOnPluginFailure]
 [-EnableFirewallRules] [-FailbackMode <FailbackType>] [-SuspendClusterNodeTimeoutMinutes <Int32>]
 [-SuspendRetriesPerNode <Int32>] [-WaitForStorageRepairTimeoutMinutes <Int32>] [-ForcePauseNoDrain]
 [-ForcePauseAndDrain] [-ForcePauseDrainAndReboot] [-SkipUpdateChecks]
 [-SiteAwareUpdatingOrder <String[]>] [-OsRollingUpgrade] [-AttemptSoftReboot]
 [-RebootMode <RebootType>] [[-ClusterName] <String>] [[-Credential] <PSCredential>] [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 有一次

```
Set-CauClusterRole [-UseDefault] [-RunOnce] [-CauPluginName <String[]>]
 [-CauPluginArguments <Hashtable[]>] [-MaxFailedNodes <Int32>] [-MaxRetriesPerNode <Int32>]
 [-NodeOrder <String[]>] [-PreUpdateScript <String>] [-PostUpdateScript <String>]
 [-ConfigurationName <String>] [-RequireAllNodesOnline] [-WarnAfter <TimeSpan>]
 [-StopAfter <TimeSpan>] [-RebootTimeoutMinutes <Int32>] [-SeparateReboots] [-RunPluginsSerially]
 [-StopOnPluginFailure] [-EnableFirewallRules] [-FailbackMode <FailbackType>]
 [-SuspendClusterNodeTimeoutMinutes <Int32>] [-SuspendRetriesPerNode <Int32>]
 [-WaitForStorageRepairTimeoutMinutes <Int32>] [-ForcePauseNoDrain] [-ForcePauseAndDrain]
 [-ForcePauseDrainAndReboot] [-SkipUpdateChecks] [-SiteAwareUpdatingOrder <String[]>]
 [-OsRollingUpgrade] [-AttemptSoftReboot] [-RebootMode <RebootType>] [[-ClusterName] <String>]
 [[-Credential] <PSCredential>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Set-CauClusterRole` cmdlet 用于设置指定集群中“集群感知更新”（Cluster-Aware Updating，简称 CAU）角色的配置属性。该 cmdlet 可以指定诸如更新计划和更新运行参数之类的属性。

要使用 **PostUpdateScript** 或 **PreUpdateScript** 参数运行此cmdlet，必须在每个节点上启用Windows PowerShell远程功能。为此，请使用 `Enable-PSRemoting` cmdlet。此外，请确保在每个节点上也启用了 **Windows Remote Management - Compatibility Mode (HTTP-In)** 防火墙例外规则。

## 示例

### 示例 1：在每月的第一周和第二周，为指定集群上的 CAU 集群角色配置相关设置

```powershell
$parameters = @{
    ClusterName = 'CONTOSO-FC1'
    DaysOfWeek = 'Tuesday'
    WeeksOfMonth = '1,2'
    RebootTimeoutMinutes = '10'
    Force = $true
}
Set-CauClusterRole $parameters
```

此命令用于配置名为 **CONTOSO-FC1** 的集群上 CAU 集群角色的相关设置。该 CAU 集群角色被设置为每月的第一周和第二周的周二执行更新操作。如果需要重启节点，系统会为每个节点预留 10 分钟的时间来完成重启；如果重启在这段时间内未能完成，则该节点上的更新操作将被标记为失败。由于命令中指定了 **Force** 参数，因此该 cmdlet 会直接运行而不会显示确认提示。

这个示例使用了“拆分”（splatting）技术，将 `$parameters` 变量中的参数值传递给命令。欲了解更多关于“拆分”的信息，请参阅 [Splatting](/powershell/module/microsoft.powershell.core/about/about_splatting)。

### 示例 2：在每月的第二周，为指定集群上的 CAU 集群角色配置相关设置

```powershell
$parameters = @{
    ClusterName = 'CONTOSO-FC1'
    DaysOfWeek = 'Tuesday'
    WeeksOfMonth = '1,2'
    IntervalWeeks = '2'
    RebootTimeoutMinutes = '10'
    PostUpdateScript = 'G:\verifyupdatesinstalled.ps1'
    Force = $true
}
Set-CauClusterRole $parameters
```

```output
Name                                                        Value
----                                                        -----
ResourceGroupName                                           CAUCAUCldy8
Status                                                      Online
StartDate                                                   10/14/2011 3:00:00 AM
PostUpdateScript                                            G:\verifyupdatesinstalled.ps1
RebootTimeoutMinutes                                        10
DaysOfWeek                                                  Tuesday
WeeksInterval                                               2
```

此命令用于配置名为**CONTOSO-FC1**的集群上CAU（Clustered Automation Update）集群角色的相关设置。该集群角色被设置为每月第二周的周二执行更新操作。如果需要重启节点，系统会为每个节点预留10分钟的时间来完成重启过程；如果重启未能在这段时间内完成，则该节点上的更新操作将被标记为失败。更新完成后，CAU集群角色会在节点退出维护模式后立即运行一个脚本（该脚本位于G盘的根目录下，文件名为`verifyupdatesinstalled.ps1`）。由于命令中指定了**Force**参数，因此该cmdlet会直接执行而不会显示确认提示。

这个示例使用了“拆分”（splatting）技术，将 `$parameters` 变量中的参数值传递给命令。欲了解更多关于“拆分”的信息，请参阅 [Splatting](/powershell/module/microsoft.powershell.core/about/about_splatting)。

### 示例 3：在指定的集群上启动更新运行

```powershell
Set-CauClusterRole -ClusterName "CONTOSO-FC1" -UpdateNow -Force
```

此命令会促使 CAU 集群角色在名为 **CONTOSO-FC1** 的集群上立即启动更新流程。由于该命令指定了 **Force** 参数，因此该 cmdlet 会在不显示确认提示的情况下直接执行。

### 示例 4：为指定集群中的 CAU 集群角色配置设置

```powershell
$WarnAfter = New-TimeSpan -hour 1 -minute 90 -seconds 10
$StopAfter = New-TimeSpan -hour 2 -minute 90 -seconds 10
$parameters = @{
    ClusterName = 'CONTOSO-FC1'
    WarnAfter = $WarnAfter
    StopAfter = $StopAfter
    StartDate = [DateTime] '1/1/2012'
    Force = $true
}
Set-CauClusterRole @parameters
```

这个示例配置了名为 **CONTOSO-FC1** 的集群上 CAU 集群角色的相关设置。示例中指定了用于记录警告信息的时间范围，以及如果更新操作未能完成时应取消该操作的规则。更新操作最早可以在 `2012/1/1` 这一天被触发。由于命令中包含了 **Force** 参数，因此该 cmdlet 会直接执行而不会显示确认提示。

这个示例使用了“拆分”（splatting）技术，将 `$parameters` 变量中的参数值传递给命令。欲了解更多关于“拆分”的信息，请参阅 [Splatting](/powershell/module/microsoft.powershell.core/about/about_splatting)。

## 参数

### -AttemptSoftReboot

表示CAU集群角色尝试对故障转移集群执行内核软重启（Kernel Soft Reboot，简称KSR）。

KSR可以绕过BIOS/固件的初始化过程。只有那些不需要进行BIOS/固件初始化的更新才能使用KSR来进行。

```yaml
Type: SwitchParameter
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
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

你可以用分号（;）分隔来指定多个配对。例如：

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

对于 `Microsoft.HotfixPlugin` 插件来说，需要以下参数：

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
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CauPluginName

指定在执行扫描或更新时使用的一个或多个插件。您可以输入多个用逗号分隔的值，默认使用的插件是 **Microsoft.WindowsUpdatePlugin**。该插件负责协调每个集群节点上安装的 Windows Update Agent 软件；该软件在从 Windows Update、Microsoft Update 或 Windows Server Update Services (WSUS) 服务器下载更新时发挥作用。有关插件如何与 CAU（Cluster-Aware Updating）协同工作的更多信息，请参阅 [How Cluster-Aware Updating plugins work](/windows-server/failover-clustering/cluster-aware-updating-plug-ins)。

```yaml
Type: String[]
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClusterName

指定用于配置 CAU 集群角色的集群名称。如果未指定，则使用当前集群。只有当此 cmdlet 不在故障转移集群节点上运行，或者用于引用与执行该 cmdlet 的位置不同的故障转移集群时，才需要此参数。

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

指定 Windows PowerShell 会话配置，该配置定义了用于运行由 **PreUpdateScript** 和 **PostUpdateScript** 参数指定的脚本及 cmdlet 的会话环境，并可以限制可运行的 cmdlet 的种类。如果指定了预更新脚本或 post 更新脚本但未指定相应的配置名称，则将使用 Windows PowerShell 内置的默认会话配置。

```yaml
Type: String
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
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

指定任务将被触发的星期几。可以指定多个值，这些值可以用逗号分隔，或者表示为十六进制数值之和。

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

该 cmdlet 的作用是：在每次 CAU 集群角色执行更新操作时（Updating Run），如果尚未启用的话，会为每个集群节点启用 **远程关机**（Remote Shutdown）的 Windows防火墙规则组。启用此规则组后，在每次更新过程中允许外部与集群节点进行通信，从而使 CAU 能够远程关闭并重新启动这些节点。如果在集群节点上使用了 Windows 防火墙但该规则组未被启用，更新操作将会失败。需要注意的是：**远程关机** 规则组的启用可能会与为 Windows 防火墙配置的 Group Policy 设置发生冲突。

```yaml
Type: SwitchParameter
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FailbackMode

指定在更新节点结束后，用于将已从该节点迁移出去的工作负载（即之前运行在该节点上但已被移动到其他节点的工作负载）重新恢复到该节点的方法。此参数的可接受值为：

- `NoFailback`
- `Immediate`
- `Policy`

The default value is `Immediate`.

```yaml
Type: FailbackType
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:
Accepted values: NoFailback, Immediate, Policy

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令运行，而无需请求用户确认。

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

这表示 CAU 集群角色会强制集群节点暂停运行，并释放所持有的角色（即让节点不再承担这些角色对应的职责）。

强制排水机制会将数据从当前负责排水的节点中转移出去，即使该组本身无法进行迁移。一个组可能无法迁移的原因在于没有其他节点能够容纳它，或者该组已经被锁定（无法被移动）。

```yaml
Type: SwitchParameter
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForcePauseDrainAndReboot

表示CAU集群角色会强制集群节点暂停运行、释放当前承担的角色，并重新启动。

强制排水机制会将数据从当前负责排水的节点中转移出去，即使该组本身无法进行迁移。一个组可能无法迁移的原因在于没有其他节点能够容纳它，或者该组已经被锁定（无法被移动）。

```yaml
Type: SwitchParameter
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForcePauseNoDrain

表示CAU集群角色强制集群节点暂停运行。这些节点的数据并不会被清除（即节点不会被“耗尽”资源）。

```yaml
Type: SwitchParameter
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IntervalWeeks

指定任务触发之间的时间间隔（以周为单位）。如果间隔为 1，则表示每周触发一次；如果间隔为 2，则表示每隔一周触发一次。

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

指定更新过程中最多允许出现故障的节点数量。如果超过这个数量的节点发生故障，更新操作将停止。该数值的范围是从 0 到集群节点总数减去 1。对于大多数集群来说，默认值约为集群节点总数的三分之一。

```yaml
Type: Int32
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxRetriesPerNode

该参数指定每个节点上更新过程（包括任何预更新和Post更新脚本）最多可以重试的次数。最大重试次数为64次，默认值为3次。

```yaml
Type: Int32
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NodeOrder

指定一个集群节点名称数组，并按照这些节点应该被更新的顺序排列它们。

```yaml
Type: String[]
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
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
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PostUpdateScript

指定一个 Windows PowerShell 脚本的路径和文件名，该脚本应在更新完成后、节点退出维护模式后立即运行。文件的扩展名必须是 `.ps1`，且路径长度加上文件名的总长度不得超过 260 个字符。作为最佳实践，该脚本应位于集群存储的磁盘上，以确保所有集群节点都能访问它。

```yaml
Type: String
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PreUpdateScript

指定一个 Windows PowerShell 脚本的路径和文件名，该脚本将在每个节点上运行，具体是在更新开始之前以及节点进入维护模式之前执行。文件的扩展名必须是 `.ps1`，并且路径与文件名的总长度不得超过 260 个字符。作为最佳实践，该脚本应存储在集群存储的磁盘上，以确保所有集群节点都能访问它。

```yaml
Type: String
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RebootMode

指定在更新过程中集群中每个节点应使用的重启类型。可用选项包括：

- `ClusProp`
- `FullReboot`
- `SoftReboot`
- `PluginCustomReboot`
- `OrchestratorDefault`

```yaml
Type: RebootType
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:
Accepted values: ClusProp, FullReboot, SoftReboot, PluginCustomReboot, OrchestratorDefault

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RebootTimeoutMinutes

指定CAU允许节点重启的最长时间（以分钟为单位）。如果节点在这段时间内未能完成重启，那么该节点上的更新操作将被标记为失败。

```yaml
Type: Int32
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RequireAllNodesOnline

表示在更新开始之前，所有集群节点都必须处于在线状态且可访问。

```yaml
Type: SwitchParameter
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RunOnce

指定 CAU（Cluster Automation Update）操作仅应执行一次，而不是按照周期性计划进行。如果您只需要对集群节点进行一次性更新，这种方式会非常有用。

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

这表示在更新过程中使用了多个插件时，CAU会扫描每个集群节点以查找适用的更新，并按照传递给**CauPluginName**参数的插件顺序对这些更新进行分组（即按插件顺序处理）。

默认情况下，CAU会并行扫描并安排所有插件所需更新的下载及安装顺序。无论该参数的配置如何，CAU都会依次为每个插件安装所需的更新。

该参数仅在 **CauPluginName** 参数中指定了多个插件时才有效。如果仅指定了一个插件，则会出现警告。

```yaml
Type: SwitchParameter
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SeparateReboots

这意味着：当某个插件在节点上安装更新时，如果该插件的更新安装需要重新启动系统，那么CAU（Cluster Automation Unit）会在每个插件完成更新安装后自动关闭并重启相应的集群节点。

该参数仅在**CauPluginName**参数中指定了多个插件时才有效。如果只指定了一个插件，系统会显示警告信息。

```yaml
Type: String[]
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
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
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StartDate

指定可以触发“更新运行”（Updating Run）的最早日期。

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

指定在更新任务（Updating Run）未完成的情况下，经过多少分钟后该任务将被取消。时间跨度可以使用 Windows PowerShell 中提供的标准格式来表示，例如 `01:30:00` 表示一小时三十分钟。默认情况下，更新任务有无限的时间来完成。

如果指定了更新前或更新后的脚本，则运行这些脚本并完成更新的全部过程必须在规定的时间限制内完成。

```yaml
Type: TimeSpan
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StopOnPluginFailure

这表示：如果在某个节点上应用更新时出现故障（无论是由哪个插件引起的），那么在“更新运行”过程中使用了多个插件的情况下，其余插件协调对该节点进行的后续更新将会被停止。

该参数仅在为 **CauPluginName** 参数指定了多个插件时才有效。如果只指定了一个插件，则会显示警告提示。

```yaml
Type: SwitchParameter
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SuspendClusterNodeTimeoutMinutes

当底层集群空间处于降级状态时，该参数指定 CAU 应等待 `Suspend-ClusterNode` cmdlet 成功的最大时间长度。

如果 `Suspend-ClusterNode` 命令因 `ERROR_CLUSTER SPACE_DEGRADED` 错误而失败，CAU 会继续重试，直到达到 `SuspendClusterNodeTimeoutMinutes` 所设定的时间限制；如果命令最终成功执行，那么重试将会停止。

这些重试操作不会减少用户设置的 **MaxRetriesPerNode** 参数的值。

超时值是针对每个集群节点而言的。因此，在最坏的情况下，CAU 可能会为集群中的每个节点花费指定时间长度。

```yaml
Type: Int32
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SuspendRetriesPerNode

指定在继续处理下一个节点之前，尝试暂停某个节点的重试次数。

```yaml
Type: Int32
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UpdateNow

指示 CAU 集群角色立即使用已配置的设置来启动更新任务（Updating Run）。

```yaml
Type: SwitchParameter
Parameter Sets: UpdateNow
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseDefault

表示对于所有没有指定值的参数，将使用默认值。

```yaml
Type: SwitchParameter
Parameter Sets: MonthlyDayOfWeek, UseDefault, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WaitForStorageRepairTimeoutMinutes

指定在继续更新之前，需要等待节点上的存储系统修复的时间长度（以分钟为单位）。

```yaml
Type: Int32
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WarnAfter

指定在更新运行（包括任何更新前和更新后的脚本）未完成后的分钟数内，会记录一条警告信息。默认情况下，无论更新运行花费了多少时间，都不会记录任何警告信息。

```yaml
Type: TimeSpan
Parameter Sets: MonthlyDayOfWeek, Weekly, Once
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WeeksOfMonth

指定每月应执行更新运行的周数。值 5 表示该月的最后一周。

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

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction和-WarningVariable。有关更多信息，请参阅[关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Add-CauClusterRole](add-cauclusterrole.md)

[禁用 CauClusterRole](disable-cauclusterrole.md)

[Enable-CauClusterRole](enable-cauclusterrole.md)

[Get-CauClusterRole](get-cauclusterrole.md)

[Remove-CauClusterRole](remove-cauclusterrole.md)
