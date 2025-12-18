---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BackgroundIntelligentTransfer.Management.dll-Help.xml
Module Name: BitsTransfer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitstransfer/add-bitsfile?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-BitsFile
---

# Add-BitsFile

## 摘要
将一个或多个文件添加到现有的BITS传输任务中。

## 语法

```
Add-BitsFile [-BitsJob] <BitsJob[]> [[-Destination] <String[]>] [-Source] <String[]> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-BitsFile` cmdlet 可将文件添加到后台智能传输服务（BITS）的传输任务中。您可以通过命令提示符或逗号分隔值（CSV）文件来指定要添加到 BITS 传输任务中的文件名称。

重要提示：一个上传作业只能包含一个文件。如果您需要上传多个文件，请使用 `Import-Csv` cmdlet，并将输出结果传递给 `Add-BitsFile` cmdlet。有关更多信息，请参阅本帮助主题中的示例 3。或者，您也可以使用 Cabinet 文件（.cab）或压缩文件（.zip）。

## 示例

### 示例 1：将一个文件添加到现有的 BITS 数据传输任务的传输队列中
```
PS C:\> Get-BitsTransfer -JobId 10778CFA-C1D7-4A82-8A9D-80B19224879C | Add-BitsFile -Source http://server01/servertestdir/testfile1.txt -Destination "c:\clienttestdir\testfile1.txt"
```

此命令会将一个文件添加到现有BITS传输任务的传输队列中。

在这个例子中，`Get-BitsTransfer` cmdlet 的输出是一个 `BitsJob` 对象，该对象通过其唯一的作业 ID 进行标识。该命令将作业 ID 传递给 `Add-BitsFile` cmdlet。文件的本地名称和远程名称作为参数传递给了 `Add-BitsFile` cmdlet。

### 示例 2：将一组文件添加到现有的 BITS 传输作业的传输队列中
```
PS C:\> $Bits = Get-BitsTransfer -JobId 10778CFA-C1D7-4A82-8A9D-80B19224879C
PS C:\> Add-BitsFile -BitsJob $Bits -Source "http://server01/servertestdir/testfile1.txt", "http://server01/servertestdir/testfile2.txt" -Destination "c:\clienttestdir\testfile1.txt", "c:\clienttestdir\testfile2.txt"
```

该命令将一组文件添加到现有BITS传输作业的传输队列中。

第一个命令根据作业ID检索对应的BITS传输任务，并将其存储在$b$变量中。第二个命令使用*BitsJob*参数，将存储在$b$变量中的**BitsJob**对象传递给**Add-BitsFile**函数。

服务器文件名与相应的客户端文件名是配对在一起的。

### 示例 3：将一组文件添加到新的 BITS（Binary Transfer Service）传输任务的传输队列中
```
PS C:\> $Bits = Start-BitsTransfer -Suspended
PS C:\> Import-CSV filelist.txt | Add-BitsFile -BitsJob $Bits
PS C:\> Resume-BitsTransfer -BitsJob $Bits
```

这个示例将一组文件添加到新的BITS传输任务的传输队列中。

第一个命令创建了一个新的 BitsJob 对象，然后将其存储在 $Bits 变量中。

第二个命令使用了 **Import-CSV** cmdlet 来导入一个包含待传输文件列表的文本文件。该文本文件会被转换成一个对象数组（每行对应一个对象），然后通过管道传递给 **Add-BitsFile** cmdlet。通过使用 *BitsJob* 参数，可以将存储在 $Bits 变量中的 **BitsJob** 对象（即传输任务）传递给 **Add-BitsFile** cmdlet。这些对象数组表示每个待下载文件的 BITS 传输任务，随后这些文件会被同时传输到客户端。此外，该命令还会使用待传输的文件列表更新传输任务的信息。

第三个命令将存储在 `$Bits` 变量中的 `BitsJob` 对象传递给 `Resume-BitsTransfer` cmdlet。BITS 数据传输任务会重新启动，然后 `Filelist.txt` 文件中指定的文件会被从源位置传输到目标位置。

第二个命令中的 `Import-CSV filelist.txt` 元素用于导入一个文本文件，该文件包含了需要传输的文件列表。文件中的每一行都使用 `<Source>,<Destination>` 的格式来指定一个待传输的文件。这个文本文件会被转换成一个对象数组（每行对应一个对象），然后传递给后续的处理流程。在这个例子中，这个对象数组被传递给了 `Add-BitsFile` cmdlet。

Filelist.txt 文件的内容类似于以下信息：

- **Source, Destination**
- `http://server01/servertestdir/testfile1.txt, c:\clienttestdir\testfile1.txt`
- `http://server01/servertestdir/testfile2.txt, c:\clienttestdir\testfile2.txt`
- `http://server01/servertestdir/testfile3.txt, c:\clienttestdir\testfile3.txt`
- `http://server01/servertestdir/testfile4.txt, c:\clienttestdir\testfile4.txt`

## 参数

### -BitsJob
指定您想要向其中添加文件的 BITS 传输作业。您可以從返回 **BitsJob** 对象的其他 cmdlet（例如 **Get-BitsTransfer**）中将该参数的值通过管道传递过来。

```yaml
Type: BitsJob[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -Destination
指定目标位置以及您想要传输的文件的名称。目标文件名与相应的源文件名一一对应。例如，*Source* 参数中指定的第一个文件名对应于 *Destination* 参数中的第一个文件名，*Source* 参数中的第二个文件名对应于 *Destination* 参数中的第二个文件名。*Source* 和 *Destination* 参数必须具有相同数量的元素；否则，该命令会生成错误。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Source
指定您想要传输的文件的源位置和文件名称。源文件名称与相应的目标文件名称一一对应。例如，*Source* 参数中指定的第一个文件名称与 *Destination* 参数中的第一个文件名称相对应，*Source* 参数中的第二个文件名称与 *Destination* 参数中的第二个文件名称相对应。*Source* 和 *Destination* 参数必须具有相同数量的元素；否则，该命令会生成错误。您可以使用标准的通配符（如星号 * 和问号 ?），或者使用范围操作符（如 \[a-r\]）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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

### Microsoft.BackgroundIntelligentTransfer.Management.BitsJob[]
此cmdlet接受一个或多个**BitsJob**对象作为输入，并将这些对象填充到*BitsJob*参数中。

## 输出

### Microsoft.BackgroundIntelligentTransfer.Management.BitsJob[]
此cmdlet会生成与BITS传输作业相关联的**BitsJob**对象，这些文件就是添加到这些传输作业中的。

## 备注

## 相关链接

[Complete-BitsTransfer](./Complete-BitsTransfer.md)

[Get-BitsTransfer](./Get-BitsTransfer.md)

[Remove-BitsTransfer](./Remove-BitsTransfer.md)

[ Resume-BitsTransfer](./Resume-BitsTransfer.md)

[Set-BitsTransfer](./Set-BitsTransfer.md)

[开始比特传输](./Start-BitsTransfer.md)

[Pause-BitsTransfer](./Suspend-BitsTransfer.md)

