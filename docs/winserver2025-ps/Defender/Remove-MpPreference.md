---
description: `Remove-MpPreference` cmdlet 用于移除针对文件名扩展名、路径和进程的排除规则，以及针对高风险、中等风险和低风险威胁的默认处理方式（即系统应采取的动作）。
external help file: MSFT_MpPreference.cdxml-help.xml
Module Name: Defender
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/defender/remove-mppreference?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-MpPreference
---

# Remove-MpPreference

## 摘要
移除排除项或默认操作。

## 语法

```
Remove-MpPreference [-ExclusionPath <String[]>] [-ExclusionExtension <String[]>] [-ExclusionProcess <String[]>]
 [-ExclusionIpAddress <String[]>] [-RealTimeScanDirection] [-QuarantinePurgeItemsAfterDelay]
 [-RemediationScheduleDay] [-RemediationScheduleTime] [-ReportingAdditionalActionTimeOut]
 [-ReportingCriticalFailureTimeOut] [-ReportingNonCriticalTimeOut] [-ScanAvgCPULoadFactor]
 [-CheckForSignaturesBeforeRunningScan] [-ScanPurgeItemsAfterDelay] [-ScanOnlyIfIdleEnabled] [-ScanParameters]
 [-ScanScheduleDay] [-ScanScheduleQuickScanTime] [-ScanScheduleTime] [-SignatureFirstAuGracePeriod]
 [-SignatureAuGracePeriod] [-SignatureDefinitionUpdateFileSharesSources]
 [-SignatureDisableUpdateOnStartupWithoutEngine] [-SignatureFallbackOrder] [-SharedSignaturesPath]
 [-SignatureScheduleDay] [-SignatureScheduleTime] [-SignatureUpdateCatchupInterval] [-SignatureUpdateInterval]
 [-SignatureBlobUpdateInterval] [-SignatureBlobFileSharesSources] [-MeteredConnectionUpdates]
 [-AllowNetworkProtectionOnWinServer] [-DisableDatagramProcessing] [-DisableCpuThrottleOnIdleScans]
 [-MAPSReporting] [-SubmitSamplesConsent] [-DisableAutoExclusions] [-DisablePrivacyMode]
 [-RandomizeScheduleTaskTimes] [-SchedulerRandomizationTime] [-DisableBehaviorMonitoring]
 [-DisableIntrusionPreventionSystem] [-DisableIOAVProtection] [-DisableRealtimeMonitoring]
 [-DisableScriptScanning] [-DisableArchiveScanning] [-DisableCatchupFullScan] [-DisableCatchupQuickScan]
 [-DisableEmailScanning] [-DisableRemovableDriveScanning] [-DisableRestorePoint]
 [-DisableScanningMappedNetworkDrivesForFullScan] [-DisableScanningNetworkFiles] [-UILockdown]
 [-ThreatIDDefaultAction_Ids <Int64[]>] [-ThreatIDDefaultAction_Actions <ThreatAction[]>]
 [-UnknownThreatDefaultAction] [-LowThreatDefaultAction] [-ModerateThreatDefaultAction]
 [-HighThreatDefaultAction] [-SevereThreatDefaultAction] [-DisableBlockAtFirstSeen] [-PUAProtection]
 [-CloudBlockLevel] [-CloudExtendedTimeout] [-EnableNetworkProtection] [-EnableControlledFolderAccess]
 [-AttackSurfaceReductionOnlyExclusions <String[]>] [-ControlledFolderAccessAllowedApplications <String[]>]
 [-ControlledFolderAccessProtectedFolders <String[]>] [-AttackSurfaceReductionRules_Ids <String[]>]
 [-AttackSurfaceReductionRules_Actions <ASRRuleActionType[]>] [-EnableLowCpuPriority]
 [-EnableFileHashComputation] [-EnableFullScanOnBatteryPower] [-ProxyPacUrl] [-ProxyServer] [-ProxyBypass]
 [-ForceUseProxyOnly] [-DisableTlsParsing] [-DisableHttpParsing] [-DisableDnsParsing]
 [-DisableDnsOverTcpParsing] [-DisableSshParsing] [-PlatformUpdatesChannel] [-EngineUpdatesChannel]
 [-SignaturesUpdatesChannel] [-DisableGradualRelease] [-AllowNetworkProtectionDownLevel]
 [-AllowDatagramProcessingOnWinServer] [-EnableDnsSinkhole] [-DisableInboundConnectionFiltering]
 [-DisableRdpParsing] [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Remove-MpPreference` cmdlet 用于移除针对文件名扩展名、路径和进程的排除规则，以及针对高风险、中等风险和低风险威胁的默认处理方式。如果您尝试移除列表中不存在的排除规则，该 cmdlet 会报告错误。

## 示例

#### 示例 1：从排除列表中移除一个文件夹
```
Remove-MpPreference -ExclusionPath "C:\Temp"
```

此命令会将文件夹 C:\Temp 从排除列表中移除。

### 示例 2：排除某个特定的文件
```
Remove-MpPreference -AttackSurfaceReductionOnlyExclusions "C:\Windows\App.exe"
```

这个命令只会排除那个特定文件夹中的 app.exe 文件。

## 参数

### -AllowDatagramProcessingOnWinServer
表示该cmdlet用于决定是否在Windows Server上禁用对UDP连接的检查功能。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: adpows

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowNetworkProtectionDownLevel
这表示该cmdlet用于在Windows 1709之前的版本中，删除允许将网络保护设置为“启用”或“审核模式”的相关设置。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: anpdl

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowNetworkProtectionOnWinServer
表示该cmdlet用于删除与Windows Server的网络保护设置相关的配置选项（即是否允许将网络保护模式设置为“Enabled”或“Audit Mode”）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: anpws

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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


### -AttackSurfaceReductionOnlyExclusions
用于指定应从攻击面缩减（Attack Surface Reduction，简称ASR）规则中排除的文件和路径。请输入需要被排除在ASR规则之外的文件夹、文件或资源名称。可以输入文件夹路径或完整的资源名。例如：“C:\Windows”会排除该目录中的所有文件；“C:\Windows\App.exe”则只会排除该特定文件夹中的那个单独文件。

有关从[自动语音识别（ASR）规则]中排除文件和文件夹的更多信息，请参阅：[/windows/security/threat-protection/microsoft-defender-atp/enable-attack-surface-reduction#exclude-files-and-folders-from-asr-rules]。

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

### -AttackSurfaceReductionRules_Actions
使用 **AttackSurfaceReductionRules_Ids** 参数来指定攻击面减少规则的状态。如果您添加了多条规则（以逗号分隔的列表形式），则需要分别以逗号分隔的列表形式指定这些规则的状态。

```yaml
Type: ASRRuleActionType[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AttackSurfaceReductionRules_Ids
使用 **AttackSurfaceReductionRules_Ids** 参数来指定攻击面减少规则的状态。如果您添加了多条规则（以逗号分隔的列表形式），则需要分别以逗号分隔的列表形式指定这些规则的状态。

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

### -CheckForSignaturesBeforeRunningScan
这表示该cmdlet会决定在Windows Defender执行扫描之前是否检查新的病毒和间谍软件定义。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: csbr

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 获得的会话对象）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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

### -CloudBlockLevel
指定云块级别（cloud block level）。该值决定了 Microsoft Defender Antivirus 在阻止和扫描可疑文件时的策略强度（即其行为的“激进程度”）。

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

### -CloudExtendedTimeout
指定用于阻止可疑文件并对其进行云扫描的额外时间长度。默认时间为10秒，最多可延长至50秒。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cloudextimeout

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControlledFolderAccessAllowedApplications
指定可以在受控文件夹中进行更改的应用程序。

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

### -ControlledFolderAccessProtectedFolders
指定更多需要保护的文件夹。

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

### -DisableArchiveScanning
该提示表示，此cmdlet可用于决定是否扫描.zip和.cab等归档文件，以检测其中是否存在恶意软件或不必要的程序。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: darchsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableAutoExclusions
表示该cmdlet用于删除与服务器相关设置：即是否禁用“自动排除”功能（Automatic Exclusions）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dae

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableBehaviorMonitoring
表示该cmdlet用于决定是否启用行为监控功能。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dbm

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableBlockAtFirstSeen
表示该 cmdlet 用于决定是否在首次看到某个内容时启用相应的阻止功能（block feature）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dbaf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableCatchupFullScan
表示该cmdlet用于控制Windows Defender是否执行计划中的全面扫描（即“追赶性扫描”）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dcfsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableCatchupQuickScan
表示该cmdlet会取消Windows Defender是否运行计划中的快速扫描（即补丁扫描）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dcqsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableCpuThrottleOnIdleScans
该提示表示：当设备处于空闲状态时，此 cmdlet 会决定是否对计划中的扫描操作进行 CPU 调节（即是否限制 CPU 的使用率）。

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

### -DisableDatagramProcessing
表示该cmdlet用于删除或启用对UDP连接进行检查的功能（即是否禁用对该类连接的检查）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ddtgp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableDnsOverTcpParsing
表示该 cmdlet 用于决定是否禁用对通过 TCP 通道传输的 DNS 流量的检测功能。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ddnstcpp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableDnsParsing
该提示表明，此 cmdlet 可用于决定是否禁用对通过 UDP 通道传输的 DNS 流量的检查功能。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ddnsp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableEmailScanning
这表明该cmdlet用于删除Windows Defender是否根据邮箱和邮件文件的具体格式来解析这些文件，以便分析邮件正文和附件的内容。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: demsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableGradualRelease
该参数表示 cmdlet 是否会禁用 Windows Defender 的月度及每日更新的渐进式发布机制。如果您启用此选项，所有更新将在渐进式发布周期结束后一次性提供给设备。对于仅接收有限更新的数据中心计算机而言，可以考虑使用此选项。

此设置同时适用于每月一次和每天一次的更新。它会覆盖之前为平台及引擎更新所配置的所有渠道选择选项。

如果您禁用或未配置此策略，设备将保持在“当前频道（默认设置）”中，除非平台及引擎更新的特定渠道中有其他规定。在该渐进式发布周期内，设备会自动保持最新状态，这适用于大多数设备。

此政策从平台版本 4.18.2106.5 及更高版本开始生效。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dgr

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableHttpParsing
表示该cmdlet用于禁用或启用对HTTP流量的检查功能。如果“EnableNetworkProtection”的值为“Enabled”，则可以阻止与恶意网站的HTTP连接。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dhttpp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableInboundConnectionFiltering
该参数表示cmdlet是否仅检查出站连接（即数据从本地系统发送到外部系统的连接）。默认情况下，Network Protection会同时检查入站和出站连接。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dicf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableIntrusionPreventionSystem
该cmdlet用于配置是否采取网络保护措施，以防止已知漏洞被利用。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dips

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableIOAVProtection
表示该 cmdlet 用于禁用/启用 Windows Defender 对所有下载的文件和附件进行扫描的功能。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dioavp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisablePrivacyMode
表示该cmdlet用于确定是否禁用隐私模式。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dpm

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableRdpParsing
该参数表示cmdlet会决定是否仅检查出站连接。默认情况下，Network Protection会同时检查入站和出站连接。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: drdpp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableRealtimeMonitoring
表示该cmdlet用于决定是否启用实时保护功能。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: drtm

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableRemovableDriveScanning
表示该cmdlet会在全面扫描过程中决定是否对可移动驱动器（如U盘）中的恶意软件和无关软件进行扫描。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: drdsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableRestorePoint
表示该cmdlet用于删除与是否禁用恢复点扫描相关的设置。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: drp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableScanningMappedNetworkDrivesForFullScan
表示该cmdlet用于决定是否扫描已映射的网络驱动器。如果您指定值为`$False`，或者不指定任何值，Windows Defender将会扫描已映射的网络驱动器。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dsmndfsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableScanningNetworkFiles
表示该cmdlet用于决定是否扫描网络文件。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dsnf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableScriptScanning
该参数用于指示cmdlet是否禁用在恶意软件扫描过程中对脚本的扫描。如果您指定值为$False，或者未指定任何值，Windows Defender将不会扫描脚本。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dscrptsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableSshParsing
表示该 cmdlet 用于决定是否禁用对 SSH 流量的检测功能。默认情况下，网络保护（Network Protection）会检测 SSH 流量。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dsshp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableTlsParsing
表示该 cmdlet 用于决定是否禁用对 TLS 流量的检查（TLS 流量也称为 HTTPS 流量）。默认情况下，网络保护功能会检测 TLS 流量。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: dtlsp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableControlledFolderAccess
表示该cmdlet会取消受控文件夹访问功能的相应设置。有效值包括：Disabled（禁用）、Enabled（启用）和Audit Mode（审计模式）。

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

### -EnableDnsSinkhole
该命令表示会清除某些设置（具体内容未在原文本中明确），从而决定是否检查DNS流量，以检测并阻止基于DNS的恶意攻击（如DNS数据泄露尝试等）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ednss

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableFileHashComputation
表示该 cmdlet 用于决定是否启用文件哈希计算功能。当此功能被启用时，Windows Defender 会为其扫描的文件计算哈希值。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: efhc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableFullScanOnBatteryPower
该信息表明，此cmdlet用于控制Windows Defender在电池供电模式下是否执行全面扫描。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: efsobp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableLowCpuPriority
表示该cmdlet用于更改Windows Defender在计划扫描时是否使用较低的CPU优先级。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: elcp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableNetworkProtection
指定网络保护服务（Network Protection Service）如何处理基于网络的恶意威胁，包括网络钓鱼和恶意软件。可能的值有：Disabled（禁用）、Enabled（启用）和AuditMode（审核模式）。

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

### -EngineUpdatesChannel
指定设备在每月逐步推送的过程中何时接收Microsoft Defender引擎更新。

有效值包括：

- NotConfigured. Devices stay up to date automatically during the gradual release cycle. This value is suitable for most devices.
- Beta. Devices are the first to receive new updates. Select Beta Channel to participate in identifying and reporting issues to Microsoft. Devices in the Windows Insider Program are subscribed to this channel by default. This value is for use in manual test environments only and a limited number of devices.
- Broad. Devices are offered updates only after the gradual release cycle completes. This value is suggested for a broad set of devices in your production population, from 10 to 100 percent.
- Preview. Devices are offered updates earliest during the monthly gradual release cycle. This value is suggested for pre-production or validation environments.
- Staged. Devices are offered updates after the monthly gradual release cycle. This value is suggested for a small, representative part of your production population, around 10 percent.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: erelr

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExclusionExtension
Specifies an array of file name extensions, such as obj or lib, to exclude from scheduled, custom, and real-time scanning.
This cmdlet removes the exclusions that you specify.

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

### -ExclusionIpAddress
Specifies an array of IP addresses to exclude from scheduled and real-time scanning.

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

### -ExclusionPath
Specifies an array of file paths to exclude from scheduled and real-time scanning.
This cmdlet removes the exclusions that you specify.

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

### -ExclusionProcess
Specifies an array of processes, as paths to process images.
This cmdlet removes exclusions of files opened by the processes that you specify.

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

### -Force
Forces the command to run without asking for user confirmation.

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

### -ForceUseProxyOnly
Removes whether to force the device to use only the proxy.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: fupo

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HighThreatDefaultAction
Indicates that this cmdlet removes the automatic remediation action specified for the high threat alert level.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: htdefac

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LowThreatDefaultAction
Indicates that this cmdlet removes the automatic remediation action specified for the low threat alert level.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ltdefac

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MAPSReporting
Indicates that the cmdlet removes membership in Microsoft Active Protection Service.

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

### -MeteredConnectionUpdates
Indicates that the cmdlet removes whether to update managed devices to update through metered connections.
Data charges may apply.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: mcupd

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ModerateThreatDefaultAction
Indicates that this cmdlet removes the automatic remediation action specified for the moderate threat alert level.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: mtdefac

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PlatformUpdatesChannel
Specifies when devices receive Microsoft Defender platform updates during the monthly gradual rollout.

有效值包括：

- NotConfigured. Devices stay up to date automatically during the gradual release cycle. This value is suitable for most devices.
- Beta. Devices are the first to receive new updates. Select Beta Channel to participate in identifying and reporting issues to Microsoft. Devices in the Windows Insider Program are subscribed to this channel by default. This value is for use in manual test environments only and a limited number of devices.
- Broad. Devices are offered updates only after the gradual release cycle completes. This value is suggested for a broad set of devices in your production population, from 10 to 100 percent.
- Preview. Devices are offered updates earliest during the monthly gradual release cycle. This value is suggested for pre-production or validation environments.
- Staged. Devices are offered updates after the monthly gradual release cycle. This value is suggested for a small, representative part of your production population, around 10 percent.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: prelr

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyBypass
Specifies proxy bypasses.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: proxbps

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyPacUrl
Specifies the Privilege Attribute Certificate (PAC) proxy.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ppurl

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProxyServer
Specifies the proxy server.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: proxsrv

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PUAProtection
Specifies the level of detection for potentially unwanted applications.
When potentially unwanted software is downloaded or attempts to install itself on your computer, you are warned.

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

### -QuarantinePurgeItemsAfterDelay
Indicates that the cmdlet removes specified number of days to keep items in the Quarantine folder.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: qpiad

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RandomizeScheduleTaskTimes
Indicates that the cmdlet removes whether to select a random time for the scheduled start and scheduled update for definitions.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: rstt

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RealTimeScanDirection
Indicates that the cmdlet removes specified scanning configuration for incoming and outgoing files on NTFS volumes.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: rtsd

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemediationScheduleDay
Indicates that the cmdlet removes specified day of the week on which to perform a scheduled full scan in order to complete remediation.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: rsd

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemediationScheduleTime
Indicates that the cmdlet removes specified time of day, as the number of minutes after midnight, to perform a scheduled scan.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: rst

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingAdditionalActionTimeOut
Indicates that the cmdlet removes specified number of minutes before a detection in the additional action state changes to the cleared state.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: raat

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingCriticalFailureTimeOut
Indicates that the cmdlet removes specified the number of minutes before a detection in the critically failed state changes to either the additional action state or the cleared state.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: rcto

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingNonCriticalTimeOut
Indicates that the cmdlet removes specified number of minutes before a detection in the non-critically failed state changes to the cleared state.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: rncto

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanAvgCPULoadFactor
Indicates that the cmdlet removes specified maximum percentage CPU usage for a scan.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: saclf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanOnlyIfIdleEnabled
Indicates that the cmdlet removes whether to start scheduled scans only when the computer is not in use.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: soiie

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanParameters
Indicates that the cmdlet removes specified scan type to use during a scheduled scan.

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

### -ScanPurgeItemsAfterDelay
Indicates that the cmdlet removes specified number of days to keep items in the scan history folder.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: spiad

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanScheduleDay
Indicates that the cmdlet removes specified the day of the week on which to perform a scheduled scan.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: scsd

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanScheduleQuickScanTime
Indicates that the cmdlet removes specified time of day, as the number of minutes after midnight, to perform a scheduled quick scan.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: scsqst

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanScheduleTime
Indicates that the cmdlet removes specified time of day, as the number of minutes after midnight, to perform a scheduled scan.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: scst

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SchedulerRandomizationTime
Specifies the randomization time for the scheduler.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: srt

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SevereThreatDefaultAction
Indicates that this cmdlet removes the automatic remediation action specified for the severe threat alert level.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: stdefac

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SharedSignaturesPath
Specifies the shared signatures path.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ssp, SecurityIntelligenceLocation, ssl

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureAuGracePeriod
Indicates that the cmdlet removes specified grace period, in minutes, for the definition.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: sigagp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureBlobFileSharesSources
Specifies the file shares sources for signatures.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: sigbfs

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureBlobUpdateInterval
Indicates that the cmdlet removes the signature update interval.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: sigbui

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureDefinitionUpdateFileSharesSources
Indicates that the cmdlet removes specified file-share sources for definition updates.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: sigdufss

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureDisableUpdateOnStartupWithoutEngine
Indicates that the cmdlet removes whether to initiate definition updates even if no antimalware engine is present.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: sigduoswo

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureFallbackOrder
Indicates that the cmdlet removes specified order in which to contact different definition update sources.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: sfo

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureFirstAuGracePeriod
Indicates that the cmdlet removes specified grace period, in minutes, for the definition.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: sigfagp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureScheduleDay
Indicates that the cmdlet removes specified day of the week on which to check for definition updates.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: sigsd

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureScheduleTime
Indicates that the cmdlet removes specified time of day, as the number of minutes after midnight, to check for definition updates.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: sigst

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignaturesUpdatesChannel
Specifies when devices receive daily Microsoft Defender definition updates during the monthly gradual rollout.

有效值包括：

- NotConfigured. Devices stay up to date automatically during the gradual release cycle. This value is suitable for most devices.
- Broad. Devices are offered updates only after the gradual release cycle completes. This value is suggested for a broad set of devices in your production population, from 10 to 100 percent.
- Staged. Devices are offered updates after the monthly gradual release cycle. This value is suggested for a small, representative part of your production population, around 10 percent.

This parameter name will be updated to **DefinitionUpdatesChannel** in a future release.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: srelr

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureUpdateCatchupInterval
Indicates that the cmdlet removes specified number of days after which Windows Defender requires a catch-up definition update.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: siguci

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureUpdateInterval
Indicates that the cmdlet removes specified interval at which to check for definition updates.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: sigui

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SubmitSamplesConsent
Indicates that the cmdlet removes how Windows Defender checks for user consent for certain samples.

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

### -ThreatIDDefaultAction_Actions
Specifies an array of the actions to take for the IDs specified by using the **ThreatIDDefaultAction_Ids** parameter.
The acceptable values for this parameter are:

- 1: Clean
- 2: Quarantine
- 3: Remove
- 6: Allow
- 8: UserDefined
- 9: NoAction
- 10: Block

>[!NOTE]
>A value of 0 (NULL) applies an action based on the Security Intelligence Update (SIU). This is the default value.

```yaml
Type: ThreatAction[]
Parameter Sets: (All)
Aliases: tiddefaca

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThreatIDDefaultAction_Ids
Specifies an array of threat IDs.
This cmdlet removes the default actions for the threat IDs that you specify.

```yaml
Type: Int64[]
Parameter Sets: (All)
Aliases: tiddefaci

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
Specifies the maximum number of concurrent operations that can be established to run the cmdlet.
If this parameter is omitted or a value of `0` is entered, then Windows PowerShell® calculates an optimum throttle limit for the cmdlet based on the number of CIM cmdlets that are running on the computer.
The throttle limit applies only to the current cmdlet, not to the session or to the computer.

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

### -UILockdown
Indicates that the cmdlet removes whether to disable UI lockdown mode.

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

### -UnknownThreatDefaultAction
表示此cmdlet会移除为未知威胁警报级别指定的自动修复操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: unktdefac

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

[Add-MpPreference](./Add-MpPreference.md)

[Get-MpPreference](./Get-MpPreference.md)

[Set-MpPreference](./Set-MpPreference.md)
