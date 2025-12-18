---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 07/01/2024
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/invoke-clusterlesscaurun?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Invoke-ClusterlessCauRun
---

# 调用 Invoke-ClusterlessCauRun 命令

## 摘要
在一组未与任何集群关联的节点上执行集群感知更新（Cluster-Aware Updating，简称CAU）操作。

## 语法

### DefaultParamSet（默认值）

```
Invoke-ClusterlessCauRun [-MaxRetries <Int32>] [-RebootTimeoutMinutes <Int32>]
 [-EnableFirewallRules] [-PreUpdateScript <String>] [-PostUpdateScript <String>]
 [-ConfigurationName <String>] [-Force] [-CauPluginName <String[]>] [-Credential <PSCredential>]
 [-CauPluginArguments <Hashtable[]>] [-RunPluginsSerially] [-StopOnPluginFailure]
 [-OsRollingUpgrade] [-RebootMode <RebootType>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 恢复参数集（RecoverParamSet）

```
Invoke-ClusterlessCauRun [-ForceRecovery] [-Force] [-Credential <PSCredential>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Invoke-ClusterlessCauRun` cmdlet 可以在一组未与集群关联的节点上执行 CAU（Cluster Assessment and Optimization）操作。该 cmdlet 适用于更新独立运行的服务器，或那些不属于任何集群的服务器组。

## 示例

### 示例 1

```powershell
Invoke-ClusterlessCauRun -MaxRetries 3
```

这个示例会在指定的节点上执行CAU（Certificate Authority Update）操作。对于每个更新失败的节点，最多会尝试重试3次。

## 参数

### -CauPluginArguments

为每个需要更新的插件指定一组名称=值的对作为参数供其使用。

例如，要为某个插件指定一个“Domain”参数：

- `@{Domain=Domain.local}`

你可以使用分号（;）来分隔多个参数对，从而在同一个集合中指定多个参数对。例如：

- `@{name1=value1;name2=value2;name3=value3}`

These name=value pairs must be meaningful to the **CauPluginName** parameter that you specify. If
you specify arguments for more than one plug-in, provide the sets of name=value pairs in the order
that you pass values in **CauPluginName**, separated by commas. For instance:

- `@{name1=value1;name2=value2;name3=value3},@{name4=value4;name5=value5}`

对于默认的 `Microsoft.WindowsUpdatePlugin` 插件，不需要任何参数。以下参数是可选的：

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
Parameter Sets: DefaultParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CauPluginName

指定在执行扫描时使用的一个或多个插件。您可以输入多个用逗号分隔的值，默认使用的插件是 **Microsoft.WindowsUpdatePlugin**。该插件负责协调每个集群节点上安装的 Windows Update Agent 软件；这种软件用于从 Windows Update、Microsoft Update 或 Windows Server Update Services (WSUS) 服务器下载更新内容时进行操作。有关插件如何与 Cluster-Aware Updating (CAU) 协同工作的更多信息，请参阅 [Cluster-Aware Updating 插件的工作原理](/windows-server/failover-clustering/cluster-aware-updating-plug-ins)。

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

### -ConfigurationName

该参数用于指定 Windows PowerShell 会话的配置信息。这些配置定义了用于运行由 **PreUpdateScript** 和 **PostUpdateScript** 参数指定的脚本以及 cmdlet 的会话环境，并且可以限制可执行的 cmdlet 的范围。如果指定了预更新脚本或 post 更新脚本，但没有指定相应的会话配置名称，则会使用 Windows PowerShell 内置的默认会话配置。

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

如果尚未启用，该操作会为每个集群节点上的 Windows 防火墙规则组“远程关机”（Remote Shutdown）功能进行配置。当指定了 `EnableFirewallRules` 参数时，CAU 会在每次执行更新任务（Updating Run）时自动重新启用“远程关机”规则组，以防在此期间该规则被手动禁用。

启用此规则组后，在每次更新过程中，每个集群节点都可以接收来自外部的通信请求；这样一来，CAU（Cluster Automation Utility）就可以远程关闭并重新启动这些节点（如果更新的安装过程需要重启节点的话）。如果在集群节点上使用了Windows防火墙，并且没有启用该规则组，那么更新操作将会失败。需要注意的是，“远程关机”功能的Windows防火墙规则组是不能被启用的——因为它会与为Windows防火墙配置的组策略设置发生冲突。

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

### -Force

强制命令执行，而无需请求用户确认。

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

### -ForceRecovery

表示该 cmdlet 从上一次失败的执行中恢复过来；那次执行导致集群处于“锁定”状态（Locked state）。

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

### -MaxRetries

指定当更新失败时，一个节点应被重试的最大次数。如果您希望确保所有节点都得到更新，那么这个设置会非常有用。

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

### -OsRollingUpgrade

这表示CAU集群角色可以在不中断Hyper-V或Scale-Out文件服务器工作负载的情况下，升级集群节点的操作系统。

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

指定一个 Windows PowerShell 脚本的路径和文件名，该脚本将在更新完成后、以及节点退出维护模式后立即在每个节点上运行。文件的扩展名必须是 `.ps1`，并且路径与文件名的总长度不得超过 260 个字符。作为最佳实践，该脚本应位于集群存储的磁盘上或高可用性的网络共享位置，以确保所有集群节点都能访问它。

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

指定一个 Windows PowerShell 脚本的路径和文件名，该脚本将在更新开始之前以及节点被置于维护模式之前在每个节点上运行。文件的扩展名必须是 `.ps1`，且路径加上文件名的总长度不得超过 260 个字符。作为最佳实践，该脚本应位于集群存储的磁盘上或高可用性的网络共享位置，以确保所有集群节点都可以访问该脚本。如果更新前的脚本执行失败，则该节点将不会被更新。

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

指定在更新过程中对集群中每个节点使用的重启类型。可用的值有：

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

指定CAU允许节点重启的最长时间（以分钟为单位）。如果节点在这段时间内未能完成重启，那么在该节点上执行的更新操作将被标记为失败。

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

### -RunPluginsSerially

这意味着在更新过程中使用多个插件时，CAU会扫描每个集群节点以查找适用的更新，并按照传递给**CauPluginName**参数的插件顺序来安排这些更新的安装。默认情况下，CAU会并行扫描并安排所有插件的适用更新；无论该参数的配置如何，CAU都会按顺序为每个插件安装相应的更新。

该参数仅在为 **CauPluginName** 参数指定了多个插件时才有效。如果只指定了一个插件，将会出现警告提示。

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

### -StopOnPluginFailure

这表示：如果在某个节点上应用更新时某个插件出现了故障，那么在“更新运行”（Updating Run）过程中同时使用多个插件的情况下，其余插件协调进行的后续更新操作将会被停止。默认情况下，一个插件的故障不会影响其他插件对该节点的更新操作。

该参数仅在为 **CauPluginName** 参数指定了多个插件时才有效。如果只指定了一个插件，将会出现警告提示。

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

### -Confirm

在运行cmdlet之前会提示您进行确认。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### Microsoft_CLUSTER AwareUpdating.ActivityIdMap

### Microsoft_CLUSTERAwareUpdating.NodeResult

### Microsoft.ClusterAware Updating.NodeStatusNotification

### Microsoft.ClusterAwareUpdating.UpdateInfo

### Microsoft-cluster Aware-Updating.UpdateInstallResult

### Microsoft_CLUSTERAwareUpdating.UpdateStagingResult

## 备注

## 相关链接

[Get-ClusterlessCauRun](get-clusterlesscaurun.md)
