---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: EventTracingManagement-help.xml
Module Name: EventTracingManagement
ms.date: 01/05/2017
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/save-etwtracesession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Save-EtwTraceSession
---

# Save-EtwTraceSession

## 摘要
将ETW会话收集到的事件保存到.etl文件中。

## 语法

```
Save-EtwTraceSession [-Name] <String> [-OutputFile <FileInfo>] [-OutputFolder <DirectoryInfo>] [-Stop]
 [-Overwrite] [-CimSession <CimSession>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Save-EtwTraceSession` cmdlet 将 ETW 会话收集到的事件保存到 `.etl` 文件中。

## 示例


## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定 ETW 会话的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OutputFile
指定用于保存ETL文件的目录，该文件将与ETW会话相关联。

```yaml
Type: FileInfo
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -OutputFolder
指定用于保存 ETW 会话生成的 `.etl` 文件的文件夹。

当设置此参数时，将根据会话属性自动选择.etl文件的名称。

如果会话处于缓冲模式，那么文件名将会与该会话的名称相同。

如果该会话是文件模式会话，那么文件名就是当前正在写入的文件的名称。

要同时控制文件名和输出文件夹，请使用 *OutputFile* 参数。

```yaml
Type: DirectoryInfo
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Overwrite
控制是否在保存本次会话时覆盖现有的文件。

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

### -Stop
控制在保存操作完成后是否应停止会话。

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

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上该cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.IO.FileInfo

### System.IO.DirectoryInfo

## 输出

### System.IO.FileInfo

此cmdlet返回一个**System.IO.FileInfo**对象，该对象表示本地计算机上的一个文件。当当前会话成功保存到本地计算机上的某个文件时，就会返回这个对象。

### CIM_DataFile

当当前会话通过CIM会话成功保存到文件时，此cmdlet会返回一个**CIM_DataFile**对象。

## 备注

## 相关链接

[Get-EtwTraceSession](./Get-EtwTraceSession.md)

[New-EtwTraceSession](./New-EtwTraceSession.md)

[Send-EtwTraceSession](./Send-EtwTraceSession.md)

[开始 ETW 追踪会话](./Start-EtwTraceSession.md)

[Stop-EtwTraceSession](./Stop-EtwTraceSession.md)

[更新-EtwTraceSession](./Update-EtwTraceSession.md)
