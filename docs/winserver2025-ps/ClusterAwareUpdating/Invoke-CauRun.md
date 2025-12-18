---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 07/01/2024
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/invoke-caurun?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Invoke-CauRun
---

# 调用 CauRun

## 摘要
对集群节点进行扫描，查找可应用的更新，并通过在该指定集群上执行“更新运行”（Updating Run）来安装这些更新。

## 语法

### DefaultParamSet（默认值）

```
Invoke-CauRun [-MaxFailedNodes <Int32>] [-MaxRetriesPerNode <Int32>] [-NodeOrder <String[]>]
 [-PreUpdateScript <String>] [-PostUpdateScript <String>] [-ConfigurationName <String>]
 [-RequireAllNodesOnline] [-WarnAfter <TimeSpan>] [-StopAfter <TimeSpan>]
 [-RebootTimeoutMinutes <Int32>] [-SeparateReboots] [-EnableFirewallRules]
 [-FailbackMode <FailbackType>] [-SuspendClusterNodeTimeoutMinutes <Int32>]
 [-SuspendRetriesPerNode <Int32>] [-WaitForStorageRepairTimeoutMinutes <Int32>] [-Force]
 [-ForcePauseNoDrain] [-ForcePauseAndDrain] [-ForcePauseDrainAndReboot] [-SkipUpdateChecks]
 [-ForceSelfUpdate] [-SiteAwareUpdatingOrder <String[]>] [[-ClusterName] <String>]
 [-AttemptSoftReboot] [-CauPluginName <String[]>] [-Credential <PSCredential>]
 [-CauPluginArguments <Hashtable[]>] [-RunPluginsSerially] [-StopOnPluginFailure]
 [-OsRollingUpgrade] [-RebootMode <RebootType>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RecoverParamSet

```
Invoke-CauRun [-ForceRecovery] [-ClearCorruptReports] [-Force] [-ForcePauseNoDrain]
 [-ForcePauseAndDrain] [-ForcePauseDrainAndReboot] [-SkipUpdateChecks] [-ForceSelfUpdate]
 [[-ClusterName] <String>] [-Credential <PSCredential>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SuspendNodeParamSet

```
Invoke-CauRun -SuspendNode <String> [-Force] [-ForcePauseNoDrain] [-ForcePauseAndDrain]
 [-ForcePauseDrainAndReboot] [-SkipUpdateChecks] [-ForceSelfUpdate] [[-ClusterName] <String>]
 [-Credential <PSCredential>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ResumeNodeParamSet

```
Invoke-CauRun -ResumeNode <String> [-Force] [-ForcePauseNoDrain] [-ForcePauseAndDrain]
 [-ForcePauseDrainAndReboot] [-SkipUpdateChecks] [-ForceSelfUpdate] [[-ClusterName] <String>]
 [-Credential <PSCredential>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Invoke-CauRun` cmdlet 会扫描集群节点以查找可应用的更新，并通过在该集群上执行的“Updating Run”操作来安装这些更新。该 “Updating Run” 过程包括以下步骤：

- Scanning for and downloading applicable updates on each cluster node.
- Moving currently running clustered roles off each cluster node.
- Installing the updates on each cluster node.
- Restarting cluster nodes if required by the installed updates.
- Moving the clustered roles back to the original nodes.
- The Updating Run process also includes ensuring that quorum is maintained, checking for additional
  updates that can only be installed after the initial set of updates are installed, and saving a
  report of the actions taken.

要使用 **PostUpdateScript** 或 **PreUpdateScript** 参数运行此 cmdlet，必须在每个节点上启用 Windows PowerShell 远程功能。为此，请运行 `Enable-PSRemoting` cmdlet。此外，请确保在每个节点上也启用了 **Windows Remote Management - Compatibility Mode (HTTP-In)** 防火墙例外规则。

## 示例

### 示例 1：在指定的集群上执行扫描操作以及完整的更新过程

```powershell
$parameters = @{
    ClusterName = 'CONTOSO-FC1'
    CauPluginName = 'Microsoft.WindowsUpdatePlugin'
    MaxFailedNodes = '1'
    MaxRetriesPerNode = '3'
    RequireAllNodesOnline = $true
    Force = $true
}
Invoke-CauRun @parameters
```

此命令会对名为 **CONTOSO-FC1** 的集群执行扫描和全面的更新操作。该 cmdlet 使用了 **Microsoft.WindowsUpdatePlugin** 插件，并要求在运行该 cmdlet 之前所有集群节点都必须处于在线状态。此外，每个节点最多只能重试三次；如果某个节点失败，则整个更新操作也会被视为失败。由于该命令指定了 **Force** 参数，因此执行过程中不会显示确认提示。

这个示例使用了“拆分（splatting）”技术，将 `$parameters` 变量中的参数值传递给命令。有关 [拆分（Splatting）] 的更多信息，请参阅 [此处](/powershell/module/microsoft.powershell.core/about/about_splatting)。

### 示例 2：使用多个插件对指定的集群执行扫描和完整更新操作

```powershell
$parameters = @{
    ClusterName = 'CONTOSO-FC1'
    CauPluginName = 'Microsoft.WindowsUpdatePlugin',
                    'Microsoft.HotfixPlugin'
    CauPluginArguments = @{ },
                         @{'HotfixRootFolderPath' = '\\CauHotfixSrv\shareName'}
    StopOnPluginFailure = $true
    EnableFirewallRules = $true
    SeparateReboots = $true
    Force = $true
}
Invoke-CauRun @parameters
```

该命令会对名为 **CONTOSO-FC1** 的集群执行扫描和全面的更新操作。此 cmdlet 使用了 **Microsoft.WindowsUpdatePlugin** 插件（采用默认配置），以及 **Microsoft.HotfixPlugin** 插件（使用 hotfix 文件夹路径 `\\CauHotfixSrv\shareName` 和默认的 hotfix 配置文件）。在开始更新操作之前，系统会先在每个集群节点上启用 **Remote Shutdown** 规则组（属于 Windows 防火墙的一部分）。如果在某个节点上使用 **Microsoft.WindowsUpdatePlugin** 安装更新时遇到故障，那么 **Microsoft.HotfixPlugin** 插件将不会尝试继续安装该更新。如果 **Microsoft.WindowsUpdatePlugin** 的安装过程需要重启节点，那么在 **Microsoft.HotfixPlugin** 进行更新之前，系统会先自动重启相关节点。由于该命令指定了 **Force** 参数，因此 cmdlet 会在不显示确认提示的情况下直接执行相应操作。

这个示例使用了“拆分（splatting）”技术，将 `$parameters` 变量中的参数值传递给命令。有关 [拆分（Splatting）] 的更多信息，请参阅 [此处](/powershell/module/microsoft.powershell.core/about/about_splatting)。

### 示例 3：从在指定集群上失败的上次更新操作中恢复

```powershell
Invoke-CauRun -ClusterName "CONTOSO-FC1" -ForceRecovery -Force
```

此命令用于恢复之前失败的更新操作，该操作导致名为 **CONTOSO-FC1** 的集群处于“锁定”状态。由于该命令指定了 **Force** 参数，因此恢复过程不会显示确认提示。

## 参数

### -AttemptSoftReboot

表示该命令尝试对故障转移集群执行内核软重启（Kernel Soft Reboot，简称KSR）。

KSR可以绕过BIOS/固件的初始化过程。因此，您只能使用KSR来执行那些不需要进行BIOS/固件初始化的更新操作。

```yaml
Type: SwitchParameter
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CauPluginArguments

为每个需要更新的插件指定一组名称=值的对作为参数供其使用。

例如，要为某个插件指定一个“Domain”参数：

- `@{Domain=Domain.local}`

你可以用分号将多个配对组合在一起来表示一组数据。例如：

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

有关默认的 **Microsoft.WindowsUpdatePlugin** 插件的查询字符串以及可以包含在查询字符串中的条件（如 IsInstalled）的更多信息，请参阅 [IUpdateSearcher::Search 方法](/windows/win32/api/wuapi/nf-wuapi-iupdatesearcher-search)。

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
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CauPluginName

指定在执行更新时使用的一个或多个插件。你可以用逗号分隔多个插件名称。默认使用的插件是 **Microsoft.WindowsUpdatePlugin**。该插件负责协调每个集群节点上运行的 Windows Update Agent 软件；当从 Windows Update、Microsoft Update 或 Windows Server Update Services (WSUS) 服务器下载更新时，也会使用相同的软件。有关插件如何与 CAU（Cluster-Aware Updating）协同工作的更多信息，请参阅 [How Cluster-Aware Updating plugins work](/windows-server/failover-clustering/cluster-aware-updating-plug-ins)。

```yaml
Type: String[]
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClearCorruptReports

指定是否清除在上次运行“集群感知更新”（Cluster-Aware Updating，简称CAU）工具期间生成的任何损坏的报告，以便从失败或中断的更新操作中恢复。

```yaml
Type: SwitchParameter
Parameter Sets: RecoverParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClusterName

指定一个集群，此cmdlet将在该集群上安装更新。

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

该参数用于指定 Windows PowerShell 会话的配置信息，这些配置信息决定了脚本运行的环境。具体的配置内容通过 **PreUpdateScript** 和 **PostUpdateScript** 参数来定义，并且可以限制可执行的 cmdlet（命令集）。如果指定了更新前的脚本或更新后的脚本，但未指定相应的配置名称，则会使用 Windows PowerShell 内置的默认会话配置。

```yaml
Type: String
Parameter Sets: DefaultParamSet
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
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableFirewallRules

如果尚未启用，该操作会为每个集群节点启用“远程关机”（Remote Shutdown）这一 Windows 防火墙规则组。当指定了 `EnableFirewallRules` 参数时，无论在两次更新任务之间是否有人手动禁用了这些规则，CAU 在执行更新操作时都会自动重新启用该规则组。

启用此规则组后，在每次更新过程中，每个集群节点都可以接受来自外部的通信；这样一来，CAU（Cloud Automation Unit）就可以远程关闭并重启相关节点（如果更新安装需要重新启动系统的话）。如果在集群节点上使用了Windows防火墙且该规则组未处于启用状态，则更新过程将会失败。需要注意的是，“Remote Shutdown”这个Windows防火墙规则组是不能被启用的，因为它会与为Windows防火墙配置的组策略设置发生冲突。

```yaml
Type: SwitchParameter
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FailbackMode

指定在更新节点完成后，用于将已被移出该节点的工作负载重新恢复到该节点上的方法。被移出的工作负载是指之前在该节点上运行过，但后来被转移到另一个节点上的工作负载。此参数的可接受值包括：

- `NoFailback`
- `Immediate`
- `Policy`

The default value is `Immediate`.

```yaml
Type: FailbackType
Parameter Sets: DefaultParamSet
Aliases:
Accepted values: NoFailback, Immediate, Policy

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令运行，而不需要用户确认。

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

表示该命令会强制集群节点暂停运行并释放其所承担的角色（即停止执行相应的任务）。

强制排水机制会将数据从负责排水的节点上“转移”出去，即使该组本身无法进行移动。某个组可能无法移动的原因在于：没有其他节点能够容纳这个组，或者该组已被锁定（无法被移动）。

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

表示该命令会强制集群节点暂停运行、释放所承担的角色（即停止执行相关任务），然后重新启动。

强制排水机制会将数据从负责排水的节点上“转移”出去，即使该组本身无法进行移动。某个组可能无法移动的原因在于：没有其他节点能够容纳这个组，或者该组已被锁定（无法被移动）。

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

表示该命令强制集群节点暂停运行。这些节点的数据并不会被清除或删除。

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

### -ForceRecovery

表示该 cmdlet 从上一次失败的运行中恢复了过来；那次失败导致集群处于“锁定”状态（Locked state）。

这个开关会破坏用于防止两个更新协调器同时意外更新同一集群的同步机制。请谨慎使用。

```yaml
Type: SwitchParameter
Parameter Sets: RecoverParamSet
Aliases: Recover

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForceSelfUpdate

指定在运行更新之前是否需要先更新本地计算机上的CAU插件。

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

### -MaxFailedNodes

指定更新操作可能失败的最大节点数。如果超过这个数量的节点出现故障，那么更新操作将会停止。该数值的范围是从 0 到集群节点总数减去 1。对于大多数集群来说，默认值大约是节点总数的三分之一。

```yaml
Type: Int32
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxRetriesPerNode

该参数指定每个节点上更新过程（包括任何预更新和后更新脚本）最多可以重试的次数。最大值为 64，默认值为 3。

```yaml
Type: Int32
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NodeOrder

指定一个集群节点名称数组，并按照这些节点被更新的顺序排列它们。

```yaml
Type: String[]
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OsRollingUpgrade

这表示CAU集群角色可以在不中断Hyper-V或Scale-Out文件服务器工作负载的情况下升级集群节点的操作系统。

```yaml
Type: SwitchParameter
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PostUpdateScript

指定一个 Windows PowerShell 脚本的路径和文件名，该脚本将在更新完成后、以及节点退出维护模式后立即在每个节点上运行。文件的扩展名必须是 `.ps1`，路径长度加上文件名的总长度不得超过 260 个字符。作为最佳实践，该脚本应位于集群存储的磁盘上或高可用性的网络共享位置，以确保所有集群节点都能访问它。

```yaml
Type: String
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PreUpdateScript

指定在更新开始之前以及节点进入维护模式之前，要在每个节点上运行的 Windows PowerShell 脚本的路径和文件名。文件的扩展名必须是 `.ps1`，且路径与文件名的总长度不得超过 260 个字符。最佳实践是将脚本放置在集群存储的磁盘上或高可用性的网络共享位置，以确保所有集群节点都能访问该脚本。如果预更新脚本失败，则该节点不会被更新。

```yaml
Type: String
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RebootMode

指定在更新过程中对集群中的每个节点使用的重启类型。可选的值有：

- `ClusProp`
- `FullReboot`
- `SoftReboot`
- `PluginCustomReboot`
- `OrchestratorDefault`

```yaml
Type: RebootType
Parameter Sets: DefaultParamSet
Aliases:
Accepted values: ClusProp, FullReboot, SoftReboot, PluginCustomReboot, OrchestratorDefault

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RebootTimeoutMinutes

指定CAU允许节点重启的时间（以分钟为单位）。如果重启在此时间内未能完成，则该节点上的更新操作将被标记为失败。

```yaml
Type: Int32
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RequireAllNodesOnline

表示在更新开始之前，所有集群节点都必须处于在线状态且可被访问。

```yaml
Type: SwitchParameter
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResumeNode

指定集群中某个节点的名称，如果该节点的更新过程之前被暂停过，则可以从中恢复更新操作。

```yaml
Type: String
Parameter Sets: ResumeNodeParamSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RunPluginsSerially

这表示在更新过程中使用多个插件时，CAU会扫描每个集群节点以查找适用的更新，并按照传递给**CauPluginName**参数的插件顺序对这些更新进行分阶段处理。默认情况下，CAU会并行扫描并分阶段处理所有插件的适用更新。无论该参数的配置如何，CAU都会按顺序安装每个插件的适用更新。

该参数仅在为 **CauPluginName** 参数指定了多个插件时才有效。如果只指定了一个插件，将会出现警告信息。

```yaml
Type: SwitchParameter
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SeparateReboots

这表示：当在更新过程中同时使用多个插件时，如果某个插件的更新安装需要节点重启，那么CAU会在每个插件完成更新安装后强制关闭该节点并重新启动它。默认情况下，在更新过程中，所有插件都会先完成对节点上的更新安装，之后节点才会进行一次重启。

该参数仅在为 **CauPluginName** 参数指定了多个插件时才有效。如果只指定了一个插件，将会出现警告信息。

```yaml
Type: SwitchParameter
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SiteAwareUpdatingOrder

指定命令更新集群节点的顺序。

默认情况下，CAU会根据节点的活动程度来决定更新节点的顺序。

```yaml
Type: String[]
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipUpdateChecks

表示该命令会跳过更新检查步骤。

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

### -StopAfter

指定更新任务（Updating Run）在未完成的情况下被取消之前的时间间隔（以分钟为单位）。该时间间隔可以使用 Windows PowerShell 中提供的标准格式来表示，例如 01:30:00 表示一小时三十分钟。默认情况下，更新任务有无限的时间来完成。

如果指定了更新前或更新后的脚本，则运行这些脚本并完成更新的全部过程必须在规定的时间限制内完成。

```yaml
Type: TimeSpan
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StopOnPluginFailure

这意味着如果在某个节点上应用更新时发生故障（无论是由哪个插件引起的），那么在更新过程中同时使用多个插件的情况下，其余插件协调进行的后续更新操作将会被停止。默认情况下，一个插件的故障不会影响其他插件对该节点的更新操作。

该参数仅在为 **CauPluginName** 参数指定了多个插件时才有效。如果只指定了一个插件，将会出现警告信息。

```yaml
Type: SwitchParameter
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SuspendClusterNodeTimeoutMinutes

如果底层的集群空间处于降级状态，该设置指定了CAU应等待`Suspend-ClusterNode` cmdlet成功执行的最大时间。

如果 `Suspend-ClusterNode` 命令因 `ERROR.cluster_space_DEGRADED` 错误而失败，CAU 会继续尝试执行该命令，直到达到 `SuspendClusterNodeTimeoutMinutes` 所设定的时间限制；或者如果命令成功执行，就会停止重试。

对于这个错误的重试次数，不会计入用户设置的 **MaxRetriesPerNode** 参数所规定的限制范围内。

超时值是针对每个集群节点设置的。因此，在最坏的情况下，CAU 可能需要为集群中的每个节点都花费指定的超时时间。

```yaml
Type: Int32
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SuspendNode

指定集群中某个节点的名称，以暂停对该节点的更新操作。

```yaml
Type: String
Parameter Sets: SuspendNodeParamSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SuspendRetriesPerNode

指定在尝试暂停某个节点后重新启动该节点的次数，直到成功或达到最大重试次数为止，之后才会继续处理下一个节点。

```yaml
Type: Int32
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WaitForStorageRepairTimeoutMinutes

指定在继续更新之前，需要等待节点上的存储问题得到修复的时间长度（以分钟为单位）。

```yaml
Type: Int32
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WarnAfter

指定在更新运行（包括任何预更新和post更新脚本）未完成后的分钟数内会记录警告的时间。默认情况下，无论更新运行花费了多少时间，都不会记录任何警告。

```yaml
Type: TimeSpan
Parameter Sets: DefaultParamSet
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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### Microsoft_CLUSTERAwareUpdatingActivityIdMap

### Microsoft-cluster Aware-Updating-cluster Result

### MicrosoftClusterAwareUpdating.NodeResult

### Microsoft_cluster Aware Updating NodeStatusNotification

### Microsoft ClusterAwareUpdating.UpdateInfo

### Microsoft Cluster Aware Updating.UpdateStagingResult

## 备注

## 相关链接

[Add-CauClusterRole](add-cauclusterrole.md)

[Get-CauRun](get-caurun.md)

[调用 Causcan](invoke-causcan.md)

[Stop-CauRun](stop-caurun.md)
