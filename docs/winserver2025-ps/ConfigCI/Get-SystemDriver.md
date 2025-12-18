---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/get-systemdriver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-SystemDriver
---

# Get-SystemDriver

## 摘要
扫描系统中的驱动程序。

## 语法

```
Get-SystemDriver [-Audit] [-ScanPath <String>] [-UserPEs] [-NoScript] [-NoShadowCopy] [-OmitPaths <String[]>]
 [-PathToCatroot <String>] [-ScriptFileNames] [<CommonParameters>]
```

## 描述
`Get-SystemDriver` cmdlet 会对系统中的所有驱动程序进行全面的扫描。该 cmdlet 会返回一个 `DriverFile` 对象，其中包含用于 `New-CIPolicyRule` 和 `New-CIPolicy` cmdlets 的相关信息。这些 cmdlets 会根据扫描到的文件来创建相应的规则。默认情况下，此 cmdlet 会递归地扫描 C:\ 目录，并仅包括内核模式下的驱动程序文件。

## 示例

### 示例 1：扫描文件夹以查找驱动程序
```
PS C:\> Get-SystemDriver -ScanPath '.\temp' -UserPEs

FilePath     : \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy9\cmdlets\temp\ConfigCI.psd1
FriendlyName : \\?\E:\cmdlets\temp\ConfigCI.psd1
FileName     :
Loaded       : False
FileVersion  :
Hash         : 1844B4531711EC9170A9D33277CE1D4FF7626C54
Hash256      : 60311157F6685727F42CC04717FEF6F905EC2A317C3B8381CDD9A79D0B184483
PageHash     :
PageHash256  :
UserMode     : True
OpusInfos    : {}
Signers      : {}

FilePath     : \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy9\cmdlets\temp\Microsoft.ConfigCI.Commands.dll
FriendlyName : \\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll
FileName     : Microsoft.ConfigCI.Commands.dll
Loaded       : False
FileVersion  : 10.0.10543.1000
Hash         : BE0777F5AF88628D4555A875036648DF1AD19BBE
Hash256      : 6FA5AF724499C338A77FEEAD90F55DDF5F23D081C6DCE8E9DF486E95C6A9B310
PageHash     : D41570F2E6E7E6245CF342131D4706C944562B1E
PageHash256  : F714D9784E15B88F56180C8EE2B40C769CC83428954585A1DCF9A260FE967CDD
UserMode     : False
OpusInfos    : {}
Signers      : {}
```

这个命令会扫描指定的文件夹，并返回一个名为**DriverFile**的对象，该对象用于生成规则。

将此对象提供给 **New-CIPolicyRule** 以创建一条规则。

### 示例 2：仅扫描 PE 文件，并排除某个文件夹
```
PS C:\> Get-SystemDriver -ScanPath '.\temp\' -UserPEs -OmitPaths '.\temp\ConfigCITestBinaries' -NoScript

FilePath     : \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy10\cmdlets\temp\Microsoft.ConfigCI.Commands.dll
FriendlyName : \\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll
FileName     : Microsoft.ConfigCI.Commands.dll
Loaded       : False
FileVersion  : 10.0.10543.1000
Hash         : BE0777F5AF88628D4555A875036648DF1AD19BBE
Hash256      : 6FA5AF724499C338A77FEEAD90F55DDF5F23D081C6DCE8E9DF486E95C6A9B310
PageHash     : D41570F2E6E7E6245CF342131D4706C944562B1E
PageHash256  : F714D9784E15B88F56180C8EE2B40C769CC83428954585A1DCF9A260FE967CDD
UserMode     : False
OpusInfos    : {}
Signers      : {}

FilePath     : \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy10\cmdlets\temp\Microsoft.ConfigCI.Commands.dll
FriendlyName : \\?\E:\cmdlets\temp\Microsoft.ConfigCI.Commands.dll
FileName     : Microsoft.ConfigCI.Commands.dll
Loaded       : False
FileVersion  : 10.0.10543.1000
Hash         : BE0777F5AF88628D4555A875036648DF1AD19BBE
Hash256      : 6FA5AF724499C338A77FEEAD90F55DDF5F23D081C6DCE8E9DF486E95C6A9B310
PageHash     : D41570F2E6E7E6245CF342131D4706C944562B1E
PageHash256  : F714D9784E15B88F56180C8EE2B40C769CC83428954585A1DCF9A260FE967CDD
UserMode     : True
OpusInfos    : {}
Signers      : {}
```

这个命令会扫描指定的文件夹，就像之前的例子一样。该命令设置了 **OmitPaths** 参数，用于排除位于 `temp ConfigCITestBinaries` 文件夹中的文件。同时，它还设置了 **NoScript** 参数，以便仅获取 PE 格式的文件的相关信息。

## 参数

### -Audit
表示此cmdlet会在代码完整性审计日志中搜索驱动程序，而不会对整个系统进行扫描。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: a

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoScript
表示该cmdlet不会扫描脚本文件，仅会搜索可移植的可执行文件（PE文件）。

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

### -NoShadowCopy
表示在扫描过程中，卷快照服务（VSS）不会对磁盘进行镜像备份。对于正在运行的系统而言，此参数可能会导致扫描无法完整完成。

如果由于目标驱动器上的磁盘空间不足导致VSS（虚拟机存储）出现错误而使扫描失败，此cmdlet会提示您指定该参数。

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

### -OmitPaths
指定一个路径数组，该cmdlet在扫描过程中会忽略这些路径。我们建议您忽略C:\Windows.old路径。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: o

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PathToCatroot
指定 CatRoot 文件夹的路径。如果要扫描远程驱动器或已挂载的驱动器，请设置此参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases: c

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScanPath
指定此cmdlet需要扫描的路径。您可以指定本地路径或远程路径。如果指定了远程驱动器或挂载的驱动器，还需要同时指定**PathToCatroot**参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases: s

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScriptFileNames

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

### -UserPEs
表示此cmdlet会在扫描过程中包含用户模式文件。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: u

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### DriverFile
此cmdlet返回一个**DriverFile**对象，其中包含生成代码完整性策略规则所需的所有驱动程序属性和证书。

## 备注

## 相关链接

[New-CIPolicy](./New-CIPolicy.md)

[New-CIPolicyRule](./New-CIPolicyRule.md)

