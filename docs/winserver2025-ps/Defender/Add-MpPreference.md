---
description: `Add-MpPreference` cmdlet 用于修改 Windows Defender 的设置。
external help file: MSFT_MpPreference.cdxml-help.xml
Module Name: Defender
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/defender/add-mppreference?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-MpPreference
---

# Add-MpPreference

## 摘要
修改Windows Defender的设置。

## 语法

```
Add-MpPreference [-ExclusionPath <String[]>] [-ExclusionExtension <String[]>]
[-ExclusionProcess <String[]>] [-ExclusionIpAddress <String[]>]
[-ThreatIDDefaultAction_Ids <Int64[]>] [-ThreatIDDefaultAction_Actions <ThreatAction[]>]
[-AttackSurfaceReductionOnlyExclusions <String[]>]
[-ControlledFolderAccessAllowedApplications <String[]>]
[-ControlledFolderAccessProtectedFolders <String[]>] [-AttackSurfaceReductionRules_Ids <String[]>]
[-AttackSurfaceReductionRules_Actions <ASRRuleActionType[]>] [-Force] [-CimSession <CimSession[]>]
[-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Add-MpPreference` cmdlet 用于修改 Windows Defender 的设置。您可以使用此 cmdlet 为文件名扩展名、路径和进程添加排除规则，并为高风险、中等风险和低风险威胁设置默认处理方式。

## 示例

### 示例 1：将一个文件夹添加到排除列表中

```powershell
Add-MpPreference -ExclusionPath 'C:\Temp'
```

这个命令将文件夹 C:\Temp 添加到排除列表中，同时会禁用 Windows Defender 对该文件夹内文件的定时扫描和实时扫描功能。

### 示例 2：允许应用程序访问文件夹

```powershell
Add-MpPreference -ControlledFolderAccessAllowedApplications 'c:\apps\test.exe'
```

此命令允许指定的应用程序在受控文件夹中进行更改。

## 参数

### -AsJob

将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

用于指定应从攻击面减少（ASR）规则中排除的文件和路径。这些文件或资源不应被ASR规则所影响。可以输入一个文件夹路径或一个完整的资源名称。例如，`C:\Windows`会排除该目录中的所有文件；而`C:\Windows\App.exe`则仅排除该特定文件夹中的那个具体文件。

有关从自动语音识别（ASR）规则中排除文件和文件夹的更多信息，请参阅[ASR规则](/windows/security/threat-protection/microsoft-defender-atp/enable-attack-surface-reduction#exclude-files-and-folders-from-asr-rules)主题。

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

使用 **AttackSurfaceReductionRules_Ids** 参数指定攻击面缩减规则的状态。如果您添加了多条规则（以逗号分隔的列表形式），则需要分别以逗号分隔的列表形式指定这些规则的状态。

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

指定用于减少攻击面的规则的ID。使用 **AttackSurfaceReductionRules_Actions** 参数来为每条规则指定状态。如果您以逗号分隔的列表形式添加了多条规则，请分别为这些规则的状态也使用逗号分隔的列表进行指定。

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

### -CimSession

在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -ExclusionExtension

指定一个文件扩展名数组（例如 `obj` 或 `lib`），以将这些文件排除在计划扫描、自定义扫描和实时扫描之外。此 cmdlet 会将这些文件扩展名添加到排除列表中。

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

指定一个IP地址数组，这些地址将被排除在计划扫描和实时扫描之外。

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

指定一个文件路径数组，这些文件路径应从计划扫描和实时扫描中排除。您可以指定一个文件夹，以排除该文件夹下的所有文件。

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

用于指定一个进程数组，这些进程用于处理图像文件。此cmdlet会将从您指定的进程中打开的文件排除在计划扫描和实时扫描之外。需要注意的是，该参数仅排除由可执行程序打开的文件，并不会排除进程本身。如果您希望排除某个特定的进程，可以使用**ExclusionPath**参数来指定该进程的路径。

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

强制命令运行，而无需请求用户确认。

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

使用 **ThreatIDDefaultAction_Ids** 参数指定要针对这些 ID 执行的操作数组。该参数的可接受值为：

- `1`: Clean
- `2`: Quarantine
- `3`: Remove
- `6`: Allow
- `8`: UserDefined
- `9`: NoAction
- `10`: Block

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

指定一个威胁ID数组。此cmdlet会为您指定的威胁ID添加默认的操作（即应对措施）。

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

指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-MpPreference](./Get-MpPreference.md)

[Remove-MpPreference](./Remove-MpPreference.md)

[Set-MpPreference](./Set-MpPreference.md)
