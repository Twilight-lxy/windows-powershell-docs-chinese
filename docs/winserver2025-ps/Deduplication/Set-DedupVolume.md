---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DedupVolume.cdxml-help.xml
Module Name: Deduplication
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/deduplication/set-dedupvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DedupVolume
---

# Set-DedupVolume

## 摘要
更改一个或多个卷上的数据去重设置。

## 语法

### 按体积统计Id（默认值）

```
Set-DedupVolume [-VolumeId <String[]>] [-OptimizeInUseFiles] [-OptimizePartialFiles]
 [-NoCompress <Boolean>] [-Verify <Boolean>] [-MinimumFileAgeDays <UInt32>]
 [-MinimumFileSize <UInt32>] [-ChunkRedundancyThreshold <UInt32>]
 [-ExcludeFolder <String[]>] [-ExcludeFileType <String[]>]
 [-ExcludeFileTypeDefault <String[]>] [-NoCompressionFileType <String[]>]
 [-InputOutputScale <UInt32>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [<CommonParameters>]
```

### 按体积统计

```
Set-DedupVolume [-Volume] <String[]> [-OptimizeInUseFiles] [-OptimizePartialFiles]
 [-NoCompress <Boolean>] [-Verify <Boolean>] [-MinimumFileAgeDays <UInt32>]
 [-MinimumFileSize <UInt32>] [-ChunkRedundancyThreshold <UInt32>]
 [-ExcludeFolder <String[]>] [-ExcludeFileType <String[]>]
 [-ExcludeFileTypeDefault <String[]>] [-NoCompressionFileType <String[]>]
 [-InputOutputScale <UInt32>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [<CommonParameters>]
```

### InputObject (cdxml)

```
Set-DedupVolume -InputObject <CimInstance[]> [-OptimizeInUseFiles] [-OptimizePartialFiles]
 [-NoCompress <Boolean>] [-Verify <Boolean>] [-MinimumFileAgeDays <UInt32>]
 [-MinimumFileSize <UInt32>] [-ChunkRedundancyThreshold <UInt32>]
 [-ExcludeFolder <String[]>] [-ExcludeFileType <String[]>]
 [-ExcludeFileTypeDefault <String[]>] [-NoCompressionFileType <String[]>]
 [-InputOutputScale <UInt32>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [<CommonParameters>]
```

## 描述

`Set-DedupVolume` cmdlet 可以更改一个或多个卷上的数据去重设置。

## 示例

### 示例 1：设置卷上的排除文件夹

```powershell
Set-DedupVolume -Volume "F:" -ExcludeFolder "F:\temp","F:\SQL"
```

此命令用于指定在数据去重过程中应跳过所有文件的根文件夹。**ExcludeFolder** 参数表示数据去重引擎会处理卷 `F:` 上所有文件夹中的文件，但会排除 Temp 文件夹和 SQL 文件夹中的文件。如果您排除了包含已优化文件的文件夹，那么该命令不会重新对这些文件进行优化；您需要手动对这些被 **ExcludeFolder** 指定的已优化文件进行重新优化操作。

请注意：如果 `ExcludeFolder` 目录中已经包含经过优化的文件，那么这些优化后的文件不会被此命令自动恢复为未优化状态。`ExcludeFolder` 下的任何先前已被优化的文件都需要手动进行去优化操作。

### 示例 2：为某个卷设置文件的最小保留期限

```powershell
Set-DedupVolume -Volume "E:" -MinimumFileAgeDays 10
```

此命令用于设置文件创建后的天数，只有在达到该天数后，去重引擎才会对文件进行优化处理。`MinimumFileAgeDays`参数指定了数据去重引擎会处理卷`E:`上所有至少在10天前创建的文件夹中的文件。

### 示例 3：为某个卷设置块冗余阈值

```powershell
Set-DedupVolume -Volume "D:" -MinimumFileAgeDays 15 -ChunkRedundancyThreshold 50
```

此命令用于设置数据去重引擎在去重过程中遇到的重复数据块的数量，之后服务器才会创建这些数据块的冗余副本。`MinimumFileAgeDays` 参数指定数据去重引擎会处理卷 `D:` 上所有至少在 15 天前创建的文件夹中的文件。`ChunkRedundancyThreshold` 参数则规定：如果数据去重引擎检测到 50 个重复的数据块，它会生成一个冗余副本作为安全措施。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 类型的 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -ChunkRedundancyThreshold

该参数指定了去重引擎在服务器创建数据块的冗余副本之前遇到的相同数据块的数量。通过为被引用最频繁的数据块增加冗余性，从而提高了服务器的可靠性。

去重功能可以检测数据损坏的情况；如果存在冗余副本，去重清理任务会从这些冗余副本中恢复损坏的数据块。默认值为 `100`，最低可设置为 `20`。如果将 **ChunkRedundancyThreshold** 参数设置得过低，会导致数据去重的效果降低（因为会生成更多冗余的数据块），同时还会消耗更多的内存和磁盘空间。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

在远程会话或远程计算机上运行该Cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认值是本地计算机上的当前会话。

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

### -ExcludeFileType

指定一个扩展类型数组，该数组中的类型将被去重引擎排除在数据去重和优化过程之外。请使用逗号分隔的值进行配置（这些值前面不应加点 `.`）。当您更改此设置时，将覆盖原有的值。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExcludeFileTypeDefault

指定一个扩展类型数组（以字符串形式表示），这些扩展类型不会被服务器优化处理。

`Enable-DedupVolume` cmdlet 会根据 **UsageType** 参数的值来修改这种行为。如果你使用该参数来修改这种行为，然后再运行 `Enable-DedupVolume`，那么这个 cmdlet 会覆盖你所做的更改。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExcludeFolder

指定一个根文件夹名称数组，在进行数据去重时，所有文件都会被忽略这些根文件夹下的文件。系统接受完整的路径，但会忽略挂载点（mount point），因为挂载点在配置后可能会发生变化。当您更改此设置时，将会覆盖原有的值。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

```yaml
Type: Microsoft.Management.Infrastructure.CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -InputOutputScale

指定在优化该卷时输入/输出并行化的程度。该参数的可接受值为从 `0` 到 `36` 的整数。默认值 `0` 会使系统根据要去重卷的大小自动选择 **InputOutputScale** 值。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumFileAgeDays

文件创建后的天数，过了这个天数后，该文件才会被视为符合优化策略（即可以用于优化过程）。

`Default` 和 `HyperV` 的 **UsageType** 将此值设置为 `3`，以便在处理热点文件或新创建的文件时最大化性能。如果您希望数据去重更加积极（即去除重复数据的速度更快），或者不介意去重所带来的额外延迟，那么您可以修改这个设置。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: MinimumFileAge

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumFileSize

指定经过优化处理的文件的最小尺寸阈值（以字节为单位）。如果文件的尺寸未达到该最小阈值，去重引擎将不会对该文件进行优化处理。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoCompress

该指示用于说明服务器在去重处理后是否会对数据进行压缩。虽然压缩会消耗更多的处理器资源，但可以节省更多存储空间。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoCompressionFileType

指定一个文件类型数组， Deduplication 引擎会排除这些类型的文件进行压缩。这些文件虽然会被去重处理，但不会被压缩，通常是因为它们的格式本身已经经过了压缩。请使用逗号分隔的字符串来列出这些文件类型（注意：字符串前面不能加上点 `.`）。更改此设置会覆盖原有的配置值。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OptimizeInUseFiles

表示服务器会尝试优化当前打开的文件。在指定此参数后，服务器可能需要等待最多15分钟才会开始优化这些文件。

`Enable-DedupVolume` 会根据 `UsageType` 参数的值来修改这种行为。如果你使用当前的参数来修改这种行为，然后再运行 `Enable-DedupVolume`，那么这个命令行工具会覆盖你所做的更改。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OptimizePartialFiles

这表示服务器会根据 `MinimumFileAgeDays` 参数的值来优化所有文件，包括那些已经存在了足够长时间的文件片段。

`Enable-DedupVolume` 会根据 `UsageType` 参数的值来修改这种行为。如果你使用当前的参数来修改这种行为，然后再运行 `Enable-DedupVolume`，那么这个命令行工具会覆盖你所做的更改。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru

返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -ThrottleLimit

指定可以同时运行的最大操作数。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -Verify

该参数用于指示去重引擎是否会对优化过程中生成的每个重复数据块进行逐字节验证，而不是仅依赖加密强度较高的哈希值来进行验证。我们不建议您使用此参数；将此参数设置为 `$True` 可能会降低优化的性能。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Volume

指定一个系统卷的数组。可以提供一个或多个卷ID、驱动器字母或卷GUID路径。对于驱动器字母，使用格式 `D:`；对于卷GUID路径，使用格式 `\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

```yaml
Type: System.String[]
Parameter Sets: ByVolume
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VolumeId

指定一个卷ID数组。

```yaml
Type: System.String[]
Parameter Sets: ByVolumeId
Aliases: DeviceId, Path, Id

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.ManagementInfrastructure.CimInstance

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名称。

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/Microsoft/Windows/Deduplication/MSFT_DedupVolume

## 备注

## 相关链接

[ Disable-DedupVolume](./Disable-DedupVolume.md)

[Enable-DedupVolume](./Enable-DedupVolume.md)

[Get-DedupVolume](./Get-DedupVolume.md)
