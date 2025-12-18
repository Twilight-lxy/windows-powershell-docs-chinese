---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 07/01/2024
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/invoke-causcan?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Invoke-CauScan
---

# 调用 CauScan

## 摘要
执行对集群节点的扫描，以查找可应用的更新，并获取将应用于指定集群中每个节点的一组初始更新列表。

## 语法

```
Invoke-CauScan [[-ClusterName] <String>] [-AttemptSoftReboot] [-CauPluginName <String[]>]
 [-Credential <PSCredential>] [-CauPluginArguments <Hashtable[]>] [-RunPluginsSerially]
 [-StopOnPluginFailure] [-OsRollingUpgrade] [-RebootMode <RebootType>] [<CommonParameters>]
```

## 描述

`Invoke-CauScan` cmdlet 用于扫描集群节点，查找可应用的更新，并获取将应用于指定集群中每个节点的初始更新列表。生成该列表可能需要几分钟的时间才能完成。

预览列表中仅包含最初的一批更新内容。该列表没有包括那些在初始更新安装之后可能会变得适用的更新。

如果指定了 **Microsoft.HotfixPlugin** 插件，扫描将仅获取在热修复文件共享位置找到的热修复文件的列表。

## 示例

### 示例 1：获取指定集群上初始更新集合的详细列表

```powershell
Invoke-CauScan -ClusterName "CONTOSO-FC1" -CauPluginName "Microsoft.WindowsUpdatePlugin" -Verbose
```

这个命令会获取一组初始更新的详细列表，这些更新目前将应用于名为 **CONTOSO-FC1** 的集群中的每个节点。该列表是基于由默认插件 **Microsoft.WindowsUpdatePlugin** 应用的更新内容生成的。预览列表中仅包含了一组初始更新，并不包括那些可能在初始更新安装之后才会生效的更新。

### 示例 2：使用查询字符串获取指定集群上初始更新集的详细列表

```powershell
$SecPasswd = ConvertTo-SecureString "PlainTextPassword" -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential ("username", $SecPasswd)
$parameters = @{
    ClusterName = 'CONTOSO-FC1'
    CauPluginName = 'Microsoft.WindowsUpdatePlugin',
                    'Microsoft.HotfixPlugin'
    CauPluginArguments = @{'QueryString'="IsInstalled=0 and Type='Software' and IsHidden=0"},
                         @{'HotfixRootFolderPath' = '\\CauHotfixSrv\shareName'}
    StopOnPluginFailure = $true
    EnableFirewallRules = $true
    Force = $true
}
Invoke-CauScan $parameters -Credential $Cred
```

这个示例会获取一组初始更新的详细列表，这些更新将当前应用于名为 **CONTOSO-FC1** 的集群中的每个节点。该列表是根据 **Microsoft.WindowsUpdatePlugin** 插件使用指定的查询字符串所应用的更新，以及在必要的热修复程序和热修复配置文件被下载到 `\\CauHotfixSrv\shareName` 之后由 **Microsoft.HotfixPlugin** 所应用的更新来生成的。此外，这个示例还展示了如何将集群 **CONTOSO-FC1** 的管理凭据传递给相应的 cmdlet。

这个示例使用“拆分”（splatting）技术将 `$parameters` 变量中的参数值传递给命令。欲了解更多关于[“拆分”技术的信息，请访问](/powershell/module/microsoft.powershell.core/about/about_splatting)。

## 参数

### -AttemptSoftReboot

表示该命令假设故障转移集群将执行内核软重启（Kernel Soft Reboot，简称KSR）。

KSR可以绕过BIOS/固件的初始化过程。只有那些不需要进行BIOS/固件初始化的更新才能使用KSR来完成。

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

为每个需要更新的插件指定一组名称=值的对作为参数使用。

例如，要为一个插件指定一个“Domain”参数：

- `@{Domain=Domain.local}`

你可以用分号（;）分隔在一组中的多对参数。例如：

- `@{name1=value1;name2=value2;name3=value3}`

These name=value pairs must be meaningful to the **CauPluginName** parameter that you specify. If
you specify arguments for more than one plug-in, provide the sets of name=value pairs in the order
that you pass values in **CauPluginName**, separated by commas. For instance:

- `@{name1=value1;name2=value2;name3=value3},@{name4=value4;name5=value5}`

对于默认的 **Microsoft.WindowsUpdatePlugin** 插件来说，不需要传递任何参数。以下参数是可选的：

- **'IncludeRecommendedUpdates'='\<Value\>'**: Boolean value to indicate that recommended updates
  will be applied in addition to important updates on each node. If not specified, the default value
  is False.
- A standard Windows Update Agent query string that specifies criteria used by the Windows Update
  Agent to filter the updates that will be applied to each node. For a name, use **QueryString** and
  for a value, enclose the full query in quotation marks. If not specified, then the
  **Microsoft.WindowsUpdatePlugin** plug-in by default uses the following argument:
- `QueryString="IsInstalled=0 and Type='Software' and IsHidden=0 and IsAssigned=1"`

有关默认的 **Microsoft.WindowsUpdatePlugin** 插件的查询字符串的更多信息，以及可以包含在查询字符串中的条件（如 IsInstalled），请参阅 [IUpdateSearcher::Search 方法](/windows/win32/api/wuapi/nf-wuapi-iupdatesearcher-search)。

对于 **Microsoft.HotfixPlugin** 插件，需要以下参数：

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

指定在执行扫描时使用的一个或多个插件。可以使用逗号分隔多个插件名称。默认使用的插件是 **Microsoft.WindowsUpdatePlugin**。该插件负责协调安装在每个集群节点上的 Windows Update Agent 软件；该软件用于在从 Windows Update、Microsoft Update 或 Windows Server Update Services (WSUS) 服务器下载更新时进行相关操作。有关插件如何与 Cluster-Aware Updating (CAU) 协同工作的更多信息，请参阅 [Cluster-Aware Updating 插件的工作原理](/windows-server/failover-clustering/cluster-aware-updating-plug-ins)。

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

指定需要扫描以查找适用更新的集群名称。仅当此cmdlet不在故障转移集群节点上运行，或者用于引用与执行该cmdlet的地点不同的故障转移集群时，才需要这个参数。

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

### -OsRollingUpgrade

这表示CAU集群角色会在不中断Hyper-V或Scale-Out文件服务器工作负载的情况下，扫描集群节点操作系统的升级需求。

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

### -RebootMode

指定在更新过程中集群中每个节点应使用的重启类型。可用的值有：

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

### -RunPluginsSerially

这表示 CAU 会扫描每个集群节点以查找可应用的更新，并按照传递给 **CauPluginName** 参数的插件顺序对每个插件进行更新处理。在更新扫描过程中，会同时使用多个插件。

默认情况下，CAU会并行扫描并处理所有插件所需的更新。只有当在**CauPluginName**参数中指定了多个插件时，此参数才有效。如果只指定了一个插件，则会出现警告提示。

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

### -StopOnPluginFailure

这表示：如果在某个节点上进行扫描时某个插件出现了故障，那么当使用多个插件进行更新扫描时，由剩余插件协调的对该节点进行的后续扫描将会被停止。

该参数仅在**CauPluginName**参数中指定了多个插件时才有效。如果只指定了一个插件，会出现警告提示。

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

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### Microsoft_clusterAwareUpdating.ActivityIdMap

### Microsoft-clusterAwareupdating.UpdateInfo

### MicrosoftCluster AwareUpdating.UpgradeSetupInfo

## 备注

## 相关链接

[Add-CauClusterRole](add-cauclusterrole.md)

[Get-CauRun](get-caurun.md)

[Invoke-CauRun](invoke-caurun.md)

[Stop-CauRun](stop-caurun.md)
