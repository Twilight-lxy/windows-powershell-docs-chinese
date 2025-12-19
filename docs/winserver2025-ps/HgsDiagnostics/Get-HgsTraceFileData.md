---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.HostGuardianService.Diagnostics.Payload.dll-Help.xml
Module Name: HgsDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsdiagnostics/get-hgstracefiledata?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-HgsTraceFileData
---

# 获取 HGS 跟踪文件数据

## 摘要
获取与HGS诊断跟踪文件相关的元数据及其内容，这些文件记录在跟踪清单（trace manifest）中。

## 语法

### 数据（默认设置）
```
Get-HgsTraceFileData -File <String> -Manifest <String> -StartByte <Int64> [<CommonParameters>]
```

### 尺寸
```
Get-HgsTraceFileData -File <String> -Manifest <String> [-Length] [<CommonParameters>]
```

## 描述
`Get-HgsTraceFileData` cmdlet 可以获取由 `Get-HgsTrace` 命令生成的 Host Guardian Service (HGS) 诊断跟踪文件中的数据段，以及这些数据的长度信息。该 cmdlet 被 `Get-HgsTrace` 命令用来通过 Windows PowerShell® 远程会话安全地读取这些跟踪文件，同时不会暴露文件系统的其他部分。

## 示例

### 示例 1：获取跟踪文件的长度
```
PS C:\> Get-TraceFileData -File "Certificates.xml" -Manifest "Traces.xml" -Length
```

这个命令用于获取名为 “Certificates.xml” 的文件的长度，该文件位于 “Traces.xml” 清单中。

### 示例 2：获取包含在清单文件中的跟踪文件片段
```
PS C:\> Get-TraceFileData -File "Logs.evtx" -Manifest "Traces.xml" -StartByte 1024
```

如果文件 Logs.evtx 存在于 Traces.xml 清单中，此命令会从该文件中读取一段数据（以字节为单位）。如果文件不存在于清单中，该 cmdlet 将返回错误。

## 参数

### -File
指定您希望查询的文件的完整路径。该文件必须位于在*Manifest*参数中指定的清单文件中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Length
这表示该 cmdlet 获取的是跟踪文件的总长度（以字节为单位），而不是某个数据段的内容。

```yaml
Type: SwitchParameter
Parameter Sets: Size
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Manifest
指定用于记录在“File”参数中指定的跟踪文件的清单文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StartByte
指定此cmdlet从哪个字节开始获取跟踪文件数据的一部分。该值必须大于0，且小于所请求文件的总长度。

```yaml
Type: Int64
Parameter Sets: Data
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于常用参数的文档（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### System.Int64

### System Byte[]

## 备注

## 相关链接

[Get-HgsTrace](./Get-HgsTrace.md)
