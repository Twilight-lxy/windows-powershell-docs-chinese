---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.HostGuardianService.Diagnostics.Payload.dll-Help.xml
Module Name: HgsDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsdiagnostics/get-hgstrace?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-HgsTrace
---

# Get-HgsTrace

## 摘要
收集并分析与受保护织物的运行相关的数据。

## 语法

### 收集（默认设置）
```
Get-HgsTrace [-Collector <String[]>] [-Target <InputTarget[]>] [[-Path] <String>] [-WriteManifest] [-Detailed]
 [-Compact] [-Diagnostic <String[]>] [<CommonParameters>]
```

### 诊断
```
Get-HgsTrace [-RunDiagnostics] [-Target <InputTarget[]>] [[-Path] <String>] [-WriteManifest] [-Detailed]
 [-Compact] [-Diagnostic <String[]>] [<CommonParameters>]
```

## 描述
`Get-HgsTrace` cmdlet 收集并分析与受保护的网络环境（guarded fabric）的运行相关的数据，诊断环境中已确认或潜在的故障，这些故障可能会影响 Host Guardian Service (HGS)、受保护的宿主以及被屏蔽的虚拟机的正常运行。

## 示例

### 示例 1：诊断本地主机
```
PS C:\> Get-HgsTrace -RunDiagnostics
```

这个命令用于诊断本地主机。相关的日志数据会被存储在一个临时文件夹中，诊断结果会反馈给用户。

### 示例 2：从指定的目标收集跟踪信息
```
PS C:\> Get-HgsTrace -Target $VMhost -Path ".\Traces"
```

该命令从在 `VMhost` 变量中指定的目标对象收集跟踪数据（trace information），然后将这些跟踪文件存储到指定的路径。由于未使用 `RunDiagnostics` 参数，因此此 cmdlet 不会对收集到的目标对象执行任何诊断操作。

### 示例 3：诊断多个目标
```
PS C:\> Get-HgsTrace -Target $VMhost,$Server -RunDiagnostics
```

此命令会对存储在 $VMHost 和 $Server 变量中的目标对象执行诊断测试。

### 示例 4：使用硬件诊断本地主机
```
PS C:\> Get-HgsTrace -RunDiagnostics -Diagnostic "Hardware"
```

此命令在本地主机上运行名为“Hardware”的诊断工具。

#### 示例 5：诊断存储在指定文件夹中的先前收集到的跟踪数据
```
PS C:\> Get-HgsTrace -RunDiagnostics -Path ".\GatheredTraces"
```

此命令会对存储在名为“GatheredTraces”的文件夹中的收集到的跟踪数据（traces）进行诊断分析。

## 参数

### -Collector
指定在收集跟踪数据时需要执行的收集器列表。当您没有指定诊断信息列表，并且未使用*RunDiagnostics*开关来运行诊断程序时，此参数用于仅收集特定的跟踪数据。

```yaml
Type: String[]
Parameter Sets: Collect
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Compact
表示所提供的输出对象应该是生成的结果集的一个最小子集，而不是整个结果集。如果提供了多个目标，则此开关参数将被忽略。

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

### -Detailed
指定输出对象应包含完整的信息，其中包括所有在默认输出报告中被省略的结果。

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

### -Diagnostic
如果您同时提供了 *RunDiagnostics* 参数，此选项会指定需要运行的诊断任务列表。如果您没有提供 *RunDiagnostics* 参数，那么该诊断任务列表将用于确定应执行哪些数据收集器（collectors）。对于那些目标系统不满足其运行要求的诊断任务或数据收集器，它们将不会被执行。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:
Accepted values: Base, All, GuardedFabric, GuardedFabricTpmMode, GuardedFabricADMode, BestPractices, GuardedHost, HostGuardianService, Networking, Https, Hardware

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定一个绝对路径或相对路径，用于存放跟踪文件（trace files）的文件夹。如果该文件夹已经存在，其中包含的任何跟踪数据都会被重新使用；如果预填充的跟踪数据中缺少某些内容，新的跟踪数据会被收集起来以补充现有的数据。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RunDiagnostics
表示会立即对收集到的跟踪数据执行诊断分析，结果集将描述对这些数据的诊断所得出的结论。

```yaml
Type: SwitchParameter
Parameter Sets: Diagnose
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Target
指定由 **New-HgsTraceTarget** 创建的目标列表，以便对这些目标进行追踪和诊断。如果未提供任何目标，但指定了一个收集路径，则系统会在该路径上查找现有的日志记录以供分析。如果没有找到符合条件的日志记录，系统会使用当前会话的凭据来访问本地主机，并根据安装的 Windows 功能推断主机的角色。

```yaml
Type: InputTarget[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WriteManifest
这表示所有收集到的跟踪文件的清单（manifest）已经生成完毕。之后可以使用 `Get-HgsTraceFileData` cmdlet 来获取关于这些跟踪文件的安全相关信息。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Windows.HostGuardianServiceDiagnosticPayload.InputTarget
这个 cmdlet 将使用 **New-HgsTraceTarget** 创建的一个或多个目标对象传递给相应的追踪和诊断工具进行处理。

## 输出

### Microsoft.Windows.HostGuardianService.Diagnostics PayloadremoteResultSet
此cmdlet返回了对提供的目标执行的各种操作和测试的结果集合。这些结果按目标和类别进行分组，每个组都有一个汇总结果，反映了所有子操作的状态。

## 备注

## 相关链接

[Get-HgsTraceFileData](./Get-HgsTraceFileData.md)

[New-HgsTraceTarget](./New-HgsTraceTarget.md)

