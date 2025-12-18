---
description: `Set-MpPreference` cmdlet 用于配置 Windows Defender 扫描和更新的偏好设置。
external help file: MSFT_MpPreference.cdxml-help.xml
Module Name: Defender
ms.date: 09/29/2025
online version: https://learn.microsoft.com/powershell/module/defender/set-mppreference?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-MpPreference
---

# Set-MpPreference

## 摘要
配置Windows Defender扫描和更新的偏好设置。

## 语法


```powershell
Set-MpPreference [-ExclusionPath <String[]>] [-ExclusionExtension <String[]>] [-ExclusionProcess <String[]>]
 [-ExclusionIpAddress <String[]>] [-RealTimeScanDirection <ScanDirection>]
 [-IntelTDTEnabled <UInt32>]
 [-QuarantinePurgeItemsAfterDelay <UInt32>] [-RemediationScheduleDay <Day>]
 [-RemediationScheduleTime <DateTime>] [-ReportingAdditionalActionTimeOut <UInt32>]
 [-ReportingCriticalFailureTimeOut <UInt32>] [-ReportingNonCriticalTimeOut <UInt32>]
 [-ScanAvgCPULoadFactor <Byte>] [-CheckForSignaturesBeforeRunningScan <Boolean>]
 [-ScanPurgeItemsAfterDelay <UInt32>] [-ScanOnlyIfIdleEnabled <Boolean>] [-ScanParameters <ScanType>]
 [-ScanScheduleDay <Day>] [-ScanScheduleQuickScanTime <DateTime>] [-ScanScheduleOffset <UInt32>]
 [-ScanScheduleTime <HH:MM:SS>]
 [-SignatureFirstAuGracePeriod <UInt32>] [-SignatureAuGracePeriod <UInt32>]
 [-SignatureDefinitionUpdateFileSharesSources <String>]
 [-SignatureDisableUpdateOnStartupWithoutEngine <Boolean>] [-SignatureFallbackOrder <String>]
 [-SharedSignaturesPath <String>] [-SignatureScheduleDay <Day>] [-SignatureScheduleTime <DateTime>]
 [-SignatureUpdateCatchupInterval <UInt32>] [-SignatureUpdateInterval <UInt32>]
 [-SignatureBlobUpdateInterval <UInt32>] [-SignatureBlobFileSharesSources <String>]
 [-MeteredConnectionUpdates <Boolean>] [-AllowNetworkProtectionOnWinServer <Boolean>]
 [-DisableDatagramProcessing <Boolean>] [-DisableCpuThrottleOnIdleScans <Boolean>]
 [-MAPSReporting <MAPSReportingType>] [-SubmitSamplesConsent <SubmitSamplesConsentType>]
 [-DisableAutoExclusions <Boolean>] [-DisablePrivacyMode <Boolean>] [-RandomizeScheduleTaskTimes <Boolean>]
 [-SchedulerRandomizationTime <UInt32>] [-DisableBehaviorMonitoring <Boolean>]
 [-DisableRealtimeMonitoring <Boolean>] [-DisableScriptScanning <Boolean>] [-DisableArchiveScanning <Boolean>] [-DisableCacheMaintenance <UInt32>]
 [-DisableCatchupFullScan <Boolean>] [-DisableCatchupQuickScan <Boolean>] [-DisableEmailScanning <Boolean>]
 [-DisableRemovableDriveScanning <Boolean>] [-DisableRestorePoint <Boolean>]
 [-DisableScanningMappedNetworkDrivesForFullScan <Boolean>] [-DisableScanningNetworkFiles <Boolean>]
 [-DisableIOAVProtection <Boolean>] [-AllowSwitchToAsyncInspection <Boolean>]
 [-UILockdown <Boolean>] [-ThreatIDDefaultAction_Ids <Int64[]>]
 [-ThreatIDDefaultAction_Actions <ThreatAction[]>] [-UnknownThreatDefaultAction <ThreatAction>]
 [-LowThreatDefaultAction <ThreatAction>] [-ModerateThreatDefaultAction <ThreatAction>]
 [-HighThreatDefaultAction <ThreatAction>] [-SevereThreatDefaultAction <ThreatAction>] [-Force]
 [-DisableBlockAtFirstSeen <Boolean>] [-PUAProtection <PUAProtectionType>]
 [-ThrottleLimit <Int32>] [-AsJob]  [<CommonParameters>] [-DisableGradualRelease <Boolean>] [-DefinitionUpdatesChannel <UpdatesChannelType>] [-EngineUpdatesChannel <UpdatesChannelType>] [-PlatformUpdatesChannel <UpdatesChannelType>][-CloudBlockLevel <CloudBlockLevelType>][-ServiceHealthReportInterval <UInt32>]
 [-CloudBlockLevel <CloudBlockLevelType>] [-CloudExtendedTimeout <UInt32>]
 [-EnableNetworkProtection <ASRRuleActionType>] [-EnableControlledFolderAccess <ControlledFolderAccessType>]
 [-AttackSurfaceReductionOnlyExclusions <String[]>] [-ControlledFolderAccessAllowedApplications <String[]>]
 [-ControlledFolderAccessProtectedFolders <String[]>] [-AttackSurfaceReductionRules_Ids <String[]>]
 [-AttackSurfaceReductionRules_Actions <ASRRuleActionType[]>] [-EnableLowCpuPriority <Boolean>]
 [-EnableFileHashComputation <Boolean>] [-EnableFullScanOnBatteryPower <Boolean>] [-ProxyPacUrl <String>]
 [-ProxyServer <String>] [-ProxyBypass <String[]>] [-ForceUseProxyOnly <Boolean>]
 [-OobeEnableRtpAndSigUpdate <Boolean>]
 [-DisableTlsParsing <Boolean>] [-DisableHttpParsing <Boolean>] [-DisableDnsParsing <Boolean>]
 [-DisableFtpParsing <Boolean>] [-DisableSmtpParsing <Boolean>]
 [-DisableDnsOverTcpParsing <Boolean>] [-DisableSshParsing <Boolean>]
 [-DisableNetworkProtectionPerfTelemetry <Boolean>]
 [-PlatformUpdatesChannel <UpdatesChannelType>] [-EngineUpdatesChannel <UpdatesChannelType>]
 [-SignaturesUpdatesChannel <UpdatesChannelType>] [-DisableGradualRelease <Boolean>]
 [-AllowNetworkProtectionDownLevel <Boolean>] [-AllowDatagramProcessingOnWinServer <Boolean>]
 [-EnableDnsSinkhole <Boolean>] [-DisableInboundConnectionFiltering <Boolean>] [-DisableRdpParsing <Boolean>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Set-MpPreference` cmdlet 用于配置 Windows Defender 的扫描和更新相关设置。您可以修改排除文件的扩展名、路径或涉及的进程，并为高、中、低威胁级别指定相应的默认处理方式。

**修复值（Remediation Values）**

下表提供了在低、中、高和严重警报级别下检测到的威胁对应的修复措施建议。

|Value |Action |
|------|-------------------------------------------------------------------------|
|1 |Clean the detected threat. |
|2 |Quarantine the detected threat. |
|3 |Remove the detected threat. |
|6 |Allow the detected threat. |
|8 |Allow the user to determine the action to take with the detected threat. |
|9 |Don't take any action. |
|10 |Block the detected threat. |
|0 | (NULL)|Apply action based on the Security Intelligence Update (SIU). This is the default value. |

## 示例

### 示例 1：安排每天检查定义更新

```sql
PS C:\> Set-MpPreference -SignatureScheduleDay Everyday
```

此命令配置了偏好设置，以便每天检查定义更新。

### 示例 2：安排一天中的某个时间来检查定义更新

```sql
PS C:\> Set-MpPreference -SignatureScheduleTime 02:00:00
```

此命令用于配置偏好设置：在安排进行检测的日子里，系统会在午夜过后120分钟自动检查定义更新情况。

## 参数

### -AllowDatagramProcessingOnWinServer
指定是否在 Windows Server 上禁用对 UDP 连接的检查功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: adpows

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowNetworkProtectionDownLevel
指定是否允许在 Windows 1709 之前的版本中将网络保护设置为“启用”（Enabled）或“审核模式”（Audit Mode）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: anpdl

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowNetworkProtectionOnWinServer
指定是否允许将Windows Server的网络保护设置为“启用”或“审核模式”。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: anpws

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```


### -AllowSwitchToAsyncInspection

指定是否启用一项性能优化功能：该功能允许在已检查并验证网络流量后，将其从同步检测模式切换到异步检测模式。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: Enabled
Accept pipeline input: False
Accept wildcard characters: False
```


### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
用于指定要从攻击面减少（Attack Surface Reduction, ASR）规则中排除的文件和路径。需要指出哪些文件夹、文件或资源应当被排除在这些规则之外。可以输入一个文件夹路径或一个完整的资源名称。例如，“C:\Windows”会排除该目录中的所有文件；而“C:\Windows/App.exe”则只会排除该特定目录中的那个单独文件。

有关从[自动语音识别（ASR）规则](/windows/security/threat-protection/microsoft-defender-atp/enable-attack-surface-reduction#exclude-files-and-folders-from-asr-rules)中排除文件和文件夹的更多信息，请参阅……

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
该设置用于指定在 Windows Defender 执行扫描之前是否需要检查新的病毒和间谍软件定义。如果指定值为 $True，则 Windows Defender 会检查新的病毒/间谍软件定义；如果指定值为 $False 或未指定任何值，扫描将使用现有的病毒/间谍软件定义进行。此设置仅适用于定时扫描，对于通过用户界面手动启动的扫描或通过命令行（使用 "mpcmdrun -Scan" 命令）执行的扫描则没有影响。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: csbr

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定云块级别（cloud block level）。该值决定了 Microsoft Defender Antivirus 在阻止和扫描可疑文件时的激进程度（即检测行为的强度）。

```yaml
Type: CloudBlockLevelType
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CloudExtendedTimeout
指定用于阻止可疑文件并对其进行云扫描的延长时间。默认时间为10秒，最长可延长至50秒。

```yaml
Type: UInt32
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
该设置用于指示是否要扫描归档文件（如.zip和.cab文件）中的恶意软件或不必要的程序。如果您指定$False的值，或者未指定任何值，Windows Defender将会扫描这些归档文件。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: darchsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableAutoExclusions
该参数用于指示是否禁用服务器的“自动排除”功能。如果您指定值为 `$False`，或者未指定任何值，Windows Defender 将为服务器启用“自动排除”功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dae

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableBehaviorMonitoring
该参数用于指示是否启用行为监控功能。如果您指定值为 `$False` 或未指定任何值，Windows Defender 将会默认启用行为监控功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dbm

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableBlockAtFirstSeen
该设置用于指示是否在首次发现恶意活动时立即启用防护措施。如果您指定值为 `$False` 或未指定任何值，Windows Defender 会自动在首次发现恶意活动时启动防护机制。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dbaf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableCacheMaintenance
用于定义缓存维护空闲任务是否执行缓存维护操作。允许的值如下：  
1 – 禁用缓存维护；  
0 – 启用缓存维护（默认值）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dcm

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableCatchupFullScan
该属性用于指示 Windows Defender 是否会为已安排的全面扫描任务执行补测（即“追赶性扫描”）。有时计算机可能会错过预定的扫描时间，通常是因为在扫描时间电脑处于关机状态。如果您将此属性的值设置为 $False，则当计算机连续两次错过预定的全面扫描后，下次有人登录该电脑时，Windows Defender 会自动执行补测。如果您将此属性的值设置为 $True，则系统不会为已安排的全面扫描任务执行任何补测操作。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dcfsc

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableCatchupQuickScan
该设置用于指示 Windows Defender 是否会为已安排的快速扫描任务执行补扫操作。有时计算机可能错过这些扫描，通常是因为在安排的时间点计算机处于关闭状态。如果您将此属性的值设置为 `$False`，那么当计算机连续两次错过已安排的快速扫描时，下次有人登录计算机时 Windows Defender 会自动执行补扫。如果您将此属性的值设置为 `$True`，则计算机将不会为已安排的快速扫描任务执行任何补扫操作。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dcqsc

Required: False
Position: Named
Default value: True
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableCpuThrottleOnIdleScans
该参数用于指示在设备处于空闲状态时，CPU是否会被限制（即进行频率调节）以执行预定的扫描任务。默认情况下此参数是启用状态的，因此无论 **ScanAvgCPULoadFactor** 的值如何设置，当设备处于空闲状态时，CPU都不会因预定扫描而被限制。对于所有其他预定的扫描任务而言，该标志没有任何影响，正常的频率调节机制仍会生效。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: None
Required: False
Position: Named
Default value: True
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableDatagramProcessing
指定是否禁用对 UDP 连接的检查功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: ddtgp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableDnsOverTcpParsing
指定是否禁用对通过 TCP 通道传输的 DNS 流量的检测。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: ddnstcpp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableDnsParsing
该参数用于指定是否禁用对通过 UDP 通道传输的 DNS 流量的检查。网络保护功能会检查通过 TCP 通道传输的 DNS 流量，以提供用于反恶意软件行为监控的元数据；或者，在设置了“-EnableDnsSinkhole”配置时，允许执行 DNS 沉洞攻击（即利用 DNS 请求进行数据窃取）。可以通过将此参数的值设置为 “$true” 来禁用该检查功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: ddnsp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableFtpParsing
指定是否为了网络保护而禁用FTP解析功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dfp

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableEmailScanning
该设置用于指示 Windows Defender 是否会根据邮件文件和附件的具体格式来解析它们，以便分析邮件正文和附件内容。Windows Defender 支持多种格式，包括 .pst、.dbx、.mbx、.mime 和 .binhex。如果您指定值为 $False 或未指定任何值，Windows Defender 会执行电子邮件扫描；如果您指定值为 $True，则 Windows Defender 将不会执行电子邮件扫描。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: demsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableGradualRelease
该选项用于指定是否禁用Windows Defender每月和每日更新的逐步推送功能。如果启用此选项，则在逐步推送周期结束后，所有更新会一次性推送给设备。对于仅接收有限更新的数据中心计算机而言，可以考虑使用这一设置。

此设置同时适用于每月更新和每日更新。它会覆盖为平台及引擎更新所配置的频道选择。

如果您禁用或不配置此策略，设备将保持在“当前频道（默认设置）”中，除非在特定频道中有其他说明。在该设备的逐步更新周期内，设备会自动保持最新状态，这对大多数设备来说都是合适的。

该政策从平台版本4.18.2106.5及更高版本开始生效。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dgr

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableHttpParsing
指定是否禁用对HTTP流量的检查功能。如果“EnableNetworkProtection”的值为“Enabled”，则可以阻止与恶意网站的HTTP连接。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dhttpp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableInboundConnectionFiltering
指定是否仅检查出站连接。默认情况下，网络保护会同时检查入站和出站连接。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dicf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableIOAVProtection
该属性用于指示 Windows Defender 是否会扫描所有下载的文件和附件。如果您指定值为 `$False`，或者未指定任何值，则默认情况下 Windows Defender 会扫描下载的文件和附件。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dioavp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableNetworkProtectionPerfTelemetry
此设置会禁用网络保护功能的数据收集与发送。可接受的取值为 0 和 1：  
- 1：禁用网络保护数据遥测功能。  
- 0（默认值）：启用网络保护数据遥测功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dnpp

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisablePrivacyMode
这是一个遗留设置，对当前平台没有任何影响。该参数的用途是禁用隐私模式——这种模式会阻止除管理员之外的用户查看威胁历史记录。当这个参数被启用时，如果你指定值为 `$False` 或没有指定任何值，隐私模式就会处于启用状态。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dpm

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableRdpParsing
此设置用于控制是否解析 RDP 流量，以检测利用 RDP 协议发起的恶意攻击。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: drdpp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableRealtimeMonitoring
该选项用于指示是否启用实时保护功能。如果您指定值为 `$False` 或未指定任何值，Windows Defender 将会默认使用实时保护功能。我们建议您启用 Windows Defender 的实时保护功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: drtm

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableRemovableDriveScanning
该设置用于指示在全面扫描过程中是否要检查可移动驱动器（如U盘）中是否存在恶意或不必要的软件。如果您指定值为 `$False`，或者未指定任何值，Windows Defender会在所有类型的扫描中都会检查可移动驱动器；如果您指定值为 `$True`，则Windows Defender在全面扫描时不会检查可移动驱动器。不过，在快速扫描或自定义扫描过程中，Windows Defender仍然可以检查可移动驱动器。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: drdsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableRestorePoint
该设置用于指示是否禁用恢复点的扫描功能。如果您指定值为 `$False` 或未指定任何值，Windows Defender 的恢复点功能将保持启用状态。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: drp, dsnf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableScanningMappedNetworkDrivesForFullScan
该参数用于指示是否扫描已映射的网络驱动器。如果您指定值为 `$False` 或未指定任何值，Windows Defender 会扫描已映射的网络驱动器；如果您指定值为 `$True`，Windows Defender 则不会扫描已映射的网络驱动器。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dsmndfsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableScanningNetworkFiles
该参数用于指示是否扫描网络文件。如果您指定值为 `$False` 或未指定任何值，Windows Defender 会扫描网络文件；如果您指定值为 `$True`，Windows Defender 将不会扫描网络文件。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dsnf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableScriptScanning
指定在恶意软件扫描过程中是否禁用脚本的扫描功能。如果您指定值为 `$False` 或未指定任何值，Windows Defender 将不会扫描脚本。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dscrptsc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableSshParsing
指定是否禁用对 SSH 流量的检查功能。默认情况下，网络保护（Network Protection）会检查 SSH 流量。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dsshp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableSmtpParsing
此设置用于禁用SMTP解析功能，以增强网络安全。允许的值包括0和1：
- -1：禁止SMTP解析。
- 0（默认值）：启用SMTP解析。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dsp

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableTlsParsing
该参数用于指定是否禁用对TLS流量的检测。网络保护功能会检查TLS流量（也称为HTTPS流量），以判断是否正在尝试连接到恶意网站，并为行为监控提供相关元数据。如果将“-EnableNetworkProtection”设置为“enabled”，则可以阻止与恶意网站的TLS连接。通过将该参数值设置為“$true”，也可以禁用HTTP流量的检测。默认情况下，网络保护功能会检查TLS流量。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: dtlsp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableControlledFolderAccess
用于指定受控文件夹访问功能的启用状态。有效值包括：Disabled（禁用）、Enabled（启用）和Audit Mode（审核模式）。

```yaml
Type: ControlledFolderAccessType
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableDnsSinkhole
该配置用于指定是否需要检查DNS流量，以检测和阻止基于DNS的恶意攻击（如DNS数据泄露企图）。网络防护机制可以监控机器的DNS流量，并结合行为分析来识别此类攻击。将此配置设置为“$true”即可启用该功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: ednss

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableFileHashComputation
指定是否启用文件哈希计算功能。当该功能被启用时，Windows Defender 会为其扫描的文件计算哈希值。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: efhc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableFullScanOnBatteryPower
指定 Windows Defender 是否在电池供电时进行完整扫描。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: efsobp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableLowCpuPriority
指定Windows Defender在计划扫描时是否使用较低的CPU优先级。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: elcp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableNetworkProtection
指定网络保护服务如何处理基于网络的恶意威胁，包括网络钓鱼和恶意软件。可选的值有：Disabled（禁用）、Enabled（启用）和AuditMode（审计模式）。

```yaml
Type: ASRRuleActionType
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EngineUpdatesChannel
指定设备在每月逐步推行的过程中接收 Microsoft Defender 引擎更新的时间。

有效值为：

- NotConfigured. Devices stay up to date automatically during the gradual release cycle. This value is suitable for most devices.
- Beta. Devices are the first to receive new updates. Select Beta Channel to participate in identifying and reporting issues to Microsoft. Devices in the Windows Insider Program are subscribed to this channel by default. This value is for use in manual test environments only and a limited number of devices.
- Broad. Devices are offered updates only after the gradual release cycle completes. This value is suggested for a broad set of devices in your production population, from 10 to 100 percent.
- Preview. Devices are offered updates earliest during the monthly gradual release cycle. This value is suggested for pre-production or validation environments.
- Staged. Devices are offered updates after the monthly gradual release cycle. This value is suggested for a small, representative part of your production population, around 10 percent.

```yaml
Type: UpdatesChannelType
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
You can specify a folder to exclude all the files under the folder.

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
This cmdlet excludes any files opened by the processes that you specify from scheduled and real-time scanning.
Specifying this parameter excludes files opened by executable programs only.
The cmdlet does not exclude the processes themselves.
To exclude a process, specify it by using the **ExclusionPath** parameter.

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
Specifies whether to force the device to use only the proxy.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: fupo

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HighThreatDefaultAction
Specifies which automatic remediation action to take for a high level threat.
The acceptable values for this parameter are:

- Quarantine
- Remove
- Ignore

```yaml
Type: ThreatAction
Parameter Sets: (All)
Aliases: htdefac
Accepted values: Clean, Quarantine, Remove, Allow, UserDefined, NoAction, Block

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IntelTDTEnabled
This policy setting configures the Intel TDT integration level for Intel TDT-capable devices.
The acceptable values for this parameter are:
- 0 (Default) - If you don't configure this setting, the default value will be applied. The default value is controlled by Microsoft security intelligence updates. Microsoft will enable Intel TDT if there is a known threat.
- 1 - If you configure this setting to enabled, Intel TDT integration will turn on.
- 2 - If you configure this setting to disabled, Intel TDT integration will turn off.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: itdte
Accepted values: 0,1 and 2

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -LowThreatDefaultAction
Specifies which automatic remediation action to take for a low level threat.
The acceptable values for this parameter are:

- Quarantine
- Remove
- Ignore

```yaml
Type: ThreatAction
Parameter Sets: (All)
Aliases: ltdefac
Accepted values: Clean, Quarantine, Remove, Allow, UserDefined, NoAction, Block

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MAPSReporting
Specifies the type of membership in Microsoft Active Protection Service.
Microsoft Active Protection Service is an online community that helps you choose how to respond to potential threats.
The community also helps prevent the spread of new malicious software.
The acceptable values for this parameter are:

- 0: Disabled.
Send no information to Microsoft.
This is the default value.
- 1: Basic membership.
Send basic information to Microsoft about detected software, including where the software came from, the actions that you apply or that apply automatically, and whether the actions succeeded.
- 2: Advanced membership.
In addition to basic information, send more information to Microsoft about malicious software, spyware, and potentially unwanted software, including the location of the software, file names, how the software operates, and how it affects your computer.

If you join this community, you can choose to automatically send basic or additional information about detected software.
Additional information helps Microsoft create new definitions.
In some instances, personal information might unintentionally be sent to Microsoft.
However, Microsoft will not use this information to identify you or contact you.

```yaml
Type: MAPSReportingType
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, Basic, Advanced

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MeteredConnectionUpdates
Specifies whether to update managed devices to update through metered connections.
Data charges may apply.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: mcupd

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ModerateThreatDefaultAction
Specifies which automatic remediation action to take for a moderate level threat.
The acceptable values for this parameter are:

- Quarantine
- Remove
- Ignore

```yaml
Type: ThreatAction
Parameter Sets: (All)
Aliases: mtdefac
Accepted values: Clean, Quarantine, Remove, Allow, UserDefined, NoAction, Block

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OobeEnableRtpAndSigUpdate

This setting allows you to configure whether real-time protection and Security Intelligence Updates are enabled during Out of Box experience (OOBE).

有效值为：
- True - If you enable this setting, real-time protection and Security Intelligence Updates are enabled during OOBE.
- False (Default) - If you either disable or don't configure this setting, real-time protection and Security Intelligence Updates during OOBE aren't enabled.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -PlatformUpdatesChannel
Specifies when devices receive Microsoft Defender platform updates during the monthly gradual rollout.

有效值为：

- NotConfigured. Devices stay up to date automatically during the gradual release cycle. This value is suitable for most devices.
- Beta. Devices are the first to receive new updates. Select Beta Channel to participate in identifying and reporting issues to Microsoft. Devices in the Windows Insider Program are subscribed to this channel by default. This value is for use in manual test environments only and a limited number of devices.
- Broad. Devices are offered updates only after the gradual release cycle completes. This value is suggested for a broad set of devices in your production population, from 10 to 100 percent.
- Preview. Devices are offered updates earliest during the monthly gradual release cycle. This value is suggested for pre-production or validation environments.
- Staged. Devices are offered updates after the monthly gradual release cycle. This value is suggested for a small, representative part of your production population, around 10 percent.

```yaml
Type: UpdatesChannelType
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
Type: String[]
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
Type: String
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
Type: String
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
Type: PUAProtectionType
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, Enabled, AuditMode

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -QuarantinePurgeItemsAfterDelay
Specifies the number of days to keep items in the Quarantine folder.
If you specify a value of zero or do not specify a value for this parameter, items stay in the Quarantine folder indefinitely.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: qpiad

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RandomizeScheduleTaskTimes
Indicates whether to select a random time for the scheduled start and scheduled update for definitions.
If you specify a value of $True or do not specify a value, scheduled tasks begin within 30 minutes, before or after, the scheduled time.
If you randomize the start times, it can distribute the impact of scanning.
For example, if several virtual machines share the same host, randomized start times prevents all the hosts from starting the scheduled tasks at the same time.

If this setting and the SchedulerRandomizationTime setting are both set to Not Configured then the system will use the default behavior of RandomizeScheduleTaskTimes, which is a 30-minute window.


```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: rstt

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RealTimeScanDirection
Specifies scanning configuration for incoming and outgoing files on NTFS volumes.
The acceptable values for this parameter are:

- 0: Scan both incoming and outgoing files.
This is the default.
- 1: Scan incoming files only.
- 2: Scan outgoing files only.

Specify a value for this parameter to enhance performance on servers which have a large number of file transfers, but need scanning for either incoming or outgoing files.
Evaluate this configuration based on the server role.
For non-NTFS volumes, Windows Defender performs full monitoring of file and program activity.

```yaml
Type: ScanDirection
Parameter Sets: (All)
Aliases: rtsd
Accepted values: Both, Incoming, Outcoming

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemediationScheduleDay
Specifies the day of the week on which to perform a scheduled full scan in order to complete remediation.
Alternatively, specify everyday for this full scan or never.
The acceptable values for this parameter are:

- 0: Everyday
- 1: Sunday
- 2: Monday
- 3: Tuesday
- 4: Wednesday
- 5: Thursday
- 6: Friday
- 7: Saturday
- 8: Never

The default value is 8, never.
If you specify a value of 8 or do not specify a value, Windows Defender performs a scheduled full scan to complete remediation by using a default frequency.

```yaml
Type: Day
Parameter Sets: (All)
Aliases: rsd
Accepted values: Everyday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Never

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RemediationScheduleTime
Specifies the time of day, as the number of minutes after midnight, to perform a scheduled scan.
The time refers to the local time on the computer.
If you do not specify a value for this parameter, a scheduled scan runs at the default time of two hours after midnight.

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases: rst

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingAdditionalActionTimeOut
Specifies the number of minutes before a detection in the additional action state changes to the cleared state.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: raat

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingCriticalFailureTimeOut
Specifies the number of minutes before a detection in the critically failed state changes to either the additional action state or the cleared state.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: rcto

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportingNonCriticalTimeOut
Specifies the number of minutes before a detection in the non-critically failed state changes to the cleared state.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: rncto

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanAvgCPULoadFactor
Specifies the maximum percentage CPU usage for a scan.
The acceptable values for this parameter are: integers from 5 through 100, and the value 0, which disables CPU throttling.
Windows Defender does not exceed the percentage of CPU usage that you specify.
The default value is 50.

Note: This is not a hard limit but rather a guidance for the scanning engine to not exceed this maximum on average. If ScanOnlyIfIdleEnabled (instructing the product to scan only when the computer is not in use) and DisableCpuThrottleOnIdleScans (instructing the product to disable CPU throttling on idle scans) are both enabled, then the value of ScanAvgCPULoadFactor is ignored.

```yaml
Type: Byte
Parameter Sets: (All)
Aliases: saclf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanOnlyIfIdleEnabled
Indicates whether to start scheduled scans only when the computer is not in use.
If you specify a value of $True or do not specify a value, Windows Defender runs schedules scans when the computer is on, but not in use.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: soiie

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanParameters
Specifies the scan type to use during a scheduled scan.
The acceptable values for this parameter are:

- 1: Quick scan
- 2: Full scan

If you do not specify this parameter, Windows Defender uses the default value of quick scan.

```yaml
Type: ScanType
Parameter Sets: (All)
Aliases:
Accepted values: QuickScan, FullScan

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanPurgeItemsAfterDelay
Specifies the number of days to keep items in the scan history folder.
After this time, Windows Defender removes the items.
If you specify a value of zero, Windows Defender does not remove items.
If you do not specify a value, Windows Defender removes items from the scan history folder after the default length of time, which is 15 days.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: spiad

Required: False
Position: Named
Default value: 15
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanScheduleDay
Specifies the day of the week on which to perform a scheduled scan.
Alternatively, specify everyday for a scheduled scan or never.
The acceptable values for this parameter are:

- 0: Everyday
- 1: Sunday
- 2: Monday
- 3: Tuesday
- 4: Wednesday
- 5: Thursday
- 6: Friday
- 7: Saturday
- 8: Never

The default value is 8, never.
If you specify a value of 8 or do not specify a value, Windows Defender does not perform scheduled scans.

```yaml
Type: Day
Parameter Sets: (All)
Aliases: scsd
Accepted values: Everyday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Never

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanScheduleQuickScanTime
Specifies the time of day, as the number of minutes after midnight, to perform a daily scheduled quick scan.
The time refers to the local time on the computer.
If you do not specify a value for this parameter, a scheduled quick scan runs at the time specified by the **ScanScheduleOffset** parameter.
That parameter has a default time of two hours after midnight.

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases: scsqst

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanScheduleOffset
Configures the number of minutes after midnight to perform a scheduled scan. The time on the endpoint is used to determine the local time. If you enable this setting, a scheduled scan will run at the time specified. If you disable or don’t enable this setting, a scheduled scan runs at the default time of two hours (120 minutes) after midnight. 

> [!TIP]
> We recommend using the **ScanScheduleOffset** parameter instead of the **ScanScheduleTime** parameter because it's a more intuitive way to set the time for the Weekly Scheduled Scan. If both **ScanScheduleOffset** and **ScanScheduleTime** are set, whichever configuration was edited more recently is used to determine the time to execute the scan.

```yaml
Type: UInt32
Aliases: scso
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanScheduleTime
Specifies the time of day to run a scheduled scan. The time refers to the local time on the computer. Specify the number of minutes after midnight (for example, enter 60 for 1 a.m.). This parameter has a default time of two hours after midnight (2 a.m.).

```yaml
Type: DateTime
Aliases: scsqst
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SchedulerRandomizationTime
Specifies the randomization time for the scheduler.

If you disable or do not configure this setting, scheduled tasks will begin at a random time within an interval of 4 hours after the specified start time.
If you enable this setting, you must pick a randomization window in hours. The possible randomization window interval is between 1 and 23 hours.

If this setting and the RandomizeScheduleTaskTimes setting are both set to Not Configured then the system will use the default behavior of RandomizeScheduleTaskTimes, which is a 30-minute window.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: srt

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ServiceHealthReportInterval
This policy setting configures the time interval (in minutes) for the service health reports to be sent from endpoints. These are for Microsoft Defender Antivirus events 1150 and 1151. For more information, see [Microsoft Defender Antivirus event IDs](/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus#microsoft-defender-antivirus-event-ids).

If you do not configure this setting, the default value will be applied. The default value is set at 60 minutes (one hour).
If you configure this setting to 0, no service health reports will be sent.
The maximum value allowed to be set is 14400 minutes (ten days).

```yaml
Type: UInt32
Aliases: shri
Accepted values: 0-14400
Position: Named
Default value: 60
Accept pipeline input: False
Accept wildcard characters: False
```

### -SevereThreatDefaultAction
Specifies which automatic remediation action to take for a severe level threat.
The acceptable values for this parameter are:

- Quarantine
- Remove
- Ignore

```yaml
Type: ThreatAction
Parameter Sets: (All)
Aliases: stdefac
Accepted values: Clean, Quarantine, Remove, Allow, UserDefined, NoAction, Block

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SharedSignaturesPath
Specifies the shared signatures path.

```yaml
Type: String
Parameter Sets: (All)
Aliases: ssp, SecurityIntelligenceLocation, ssl

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureAuGracePeriod
Specifies a grace period, in minutes, for the definition.
If a definition successfully updates within this period, Windows Defender abandons any service initiated updates.

```yaml
Type: UInt32
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
Type: String
Parameter Sets: (All)
Aliases: sigbfs

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureBlobUpdateInterval
Specifies the signature update interval.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: sigbui

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureDefinitionUpdateFileSharesSources
Specifies file-share sources for definition updates.
Specify sources as a sequence of Universal Naming Convention (UNC) locations, separated by the pipeline symbol; for example, `"\\Server01\Share01 | \\Server02\Share02 | \\Server03\Share03"`.
If you specify a value for this parameter, Windows Defender attempts to connect to the shares in the order that you specify.
After Windows Defender updates a definition, it stops attempting to connect to shares on the list.
If you do not specify a value for this parameter, the list is empty.

```yaml
Type: String
Parameter Sets: (All)
Aliases: sigdufss

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureDisableUpdateOnStartupWithoutEngine
Indicates whether to initiate definition updates even if no antimalware engine is present.
If you specify a value of $True or do not specify a value, Windows Defender does not initiate definition updates on startup.
If you specify a value of $False, and if no antimalware engine is present, Windows Defender initiates definition updates on startup.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: sigduoswo

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureFallbackOrder
Specifies the order in which to contact different definition update sources.
Specify the types of update sources in the order in which you want Windows Defender to contact them, separated by the pipeline symbol; for example, `"InternalDefinitionUpdateServer | MicrosoftUpdateServer | MMPC"`.
The values that you can specify in the string are:

- InternalDefinitionUpdateServer
- MicrosoftUpdateServer
- MMPC
- FileShares

MMPC refers to Microsoft Malware Protection Center.

If you specify a value for this parameter, Windows Defender contacts the definition update sources in the specified order.
After Windows Defender downloads definition updates from a source, it stops attempting to connect to other sources.
If you do not specify a value for this parameter, Windows Defender contacts sources in the default order of `"MicrosoftUpdateServer | MMPC"`.

```yaml
Type: String
Parameter Sets: (All)
Aliases: sfo

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureFirstAuGracePeriod
Specifies a grace period, in minutes, for the definition.
If a definition successfully updates within this period, Windows Defender abandons any service initiated updates.
This parameter overrides the value of the **CheckForSignaturesBeforeRunningScan** parameter.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: sigfagp

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureScheduleDay
Specifies the day of the week on which to check for definition updates.
Alternatively, specify everyday for a scheduled scan or never.
The acceptable values for this parameter are:

- 0: Everyday
- 1: Sunday
- 2: Monday
- 3: Tuesday
- 4: Wednesday
- 5: Thursday
- 6: Friday
- 7: Saturday
- 8: Never

The default value is 8, never.
If you specify a value of 8 or do not specify a value, Windows Defender checks for definition updates by using a default frequency.

```yaml
Type: Day
Parameter Sets: (All)
Aliases: sigsd
Accepted values: Everyday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Never

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureScheduleTime
Specifies the time of day, as the number of minutes after midnight, to check for definition updates.
The time refers to the local time on the computer.
If you do not specify a value for this parameter, Windows Defender checks for definition updates at the default time of 15 minutes before the scheduled scan time.

```yaml
Type: DateTime
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

有效值为：

- NotConfigured. Devices stay up to date automatically during the gradual release cycle. This value is suitable for most devices.
- Broad. Devices are offered updates only after the gradual release cycle completes. This value is suggested for a broad set of devices in your production population, from 10 to 100 percent.
- Staged. Devices are offered updates after the monthly gradual release cycle. This value is suggested for a small, representative part of your production population, around 10 percent.

This parameter name will be updated to **DefinitionUpdatesChannel** in a future release.

```yaml
Type: UpdatesChannelType
Parameter Sets: (All)
Aliases: srelr

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureUpdateCatchupInterval
Specifies the number of days after which Windows Defender requires a catch-up definition update.
If you do not specify a value for this parameter, Windows Defender requires a catch-up definition update after the default value of one day.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: siguci

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureUpdateInterval
Specifies the interval, in hours, at which to check for definition updates.
The acceptable values for this parameter are: integers from 1 through 24.
If you do not specify a value for this parameter, Windows Defender checks at the default interval.
You can use this parameter instead of the **SignatureScheduleDay** parameter and **SignatureScheduleTime** parameter.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: sigui

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SubmitSamplesConsent
Specifies how Windows Defender checks for user consent for certain samples.
If consent has previously been granted, Windows Defender submits the samples.
Otherwise, if the **MAPSReporting** parameter does not have a value of Disabled, Windows Defender prompts the user for consent.
The acceptable values for this parameter are:

- 0: Always prompt
- 1: Send safe samples automatically
- 2: Never send
- 3: Send all samples automatically

```yaml
Type: SubmitSamplesConsentType
Parameter Sets: (All)
Aliases:
Accepted values: AlwaysPrompt, SendSafeSamples, NeverSend, SendAllSamples

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
Accepted values: Clean, Quarantine, Remove, Allow, UserDefined, NoAction, Block

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThreatIDDefaultAction_Ids
Specifies an array of threat IDs.
This cmdlet modifies the default action for the threat IDs that you specify.

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

### -ThrottleForScheduledScanOnly
A CPU usage limit can be applied to scheduled scans only, or to scheduled and custom scans. The default value applies a CPU usage limit to scheduled scans only.
The acceptable values for this parameter are:
- 1 (Default) - If you enable this setting, CPU throttling will apply only to scheduled scans.
- 0 - If you disable this setting, CPU throttling will apply to scheduled and custom scans.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 1
Accept pipeline input: False
Accept wildcard characters: False
```


### -UILockdown
Indicates whether to disable UI lockdown mode.
If you specify a value of $True, Windows Defender disables UI lockdown mode.
If you specify $False or do not specify a value, UI lockdown mode is enabled.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UnknownThreatDefaultAction
Specifies which automatic remediation action to take for an unknown level threat.
The acceptable values for this parameter are:

- Quarantine
- Remove
- Ignore

```yaml
Type: ThreatAction
Parameter Sets: (All)
Aliases: unktdefac
Accepted values: Clean, Quarantine, Remove, Allow, UserDefined, NoAction, Block

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

## 输出

## 备注

## 相关链接

[Add-MpPreference](./Add-MpPreference.md)

[Get-MpPreference](./Get-MpPreference.md)

[Remove-MpPreference](./Remove-MpPreference.md)

