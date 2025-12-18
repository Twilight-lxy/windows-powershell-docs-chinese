---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrbacklog?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrBacklog
---

# Get-DfsrBacklog

## 摘要
检索两个DFS复制伙伴之间待处理的文件更新列表。

## 语法

```
Get-DfsrBacklog [[-GroupName] <String[]>] [[-FolderName] <String[]>] [-SourceComputerName] <String>
 [-DestinationComputerName] <String> [<CommonParameters>]
```

## 描述
`Get-DfrsBacklog` cmdlet 可以检索参与分布式文件系统（DFS）复制的两台计算机之间尚未完成的更新操作。

更新可以包括新文件、修改后的文件或删除的文件及文件夹。该命令最多能显示 100 个文件。`**Verbose**` 参数会显示所有待处理的更新的数量。DFS 复制任务列表中出现的任何文件或文件夹都尚未从源计算机复制到目标计算机。这并不一定表示存在问题；待处理的任务列表只是反映了复制过程中的延迟现象。根据配置、数据变化频率、网络状况等因素，您的环境中出现这种延迟是正常的。

## 示例

### 示例 1：检索未复制的更改
```powershell
PS C:\> Get-DfsrBacklog -DestinationComputerName "SRV01" -SourceComputerName "SRV02" -GroupName "RG01" -FolderName "RF1A"
```
```output
Identifier                  : {DCE7FC28-5584-4D5D-BC84-2BD9D53CC2FC}-v538
Flags                       : 5
Attributes                  : 32
GlobalVersionSequenceNumber : {DCE7FC28-5584-4D5D-BC84-2BD9D53CC2FC}-v538
UpdateSequenceNumber        : 71576496
ParentId                    : {997D8F76-1207-49D7-85C9-DED015105A2F}-v1
FileId                      : 562949953495210
Volume                      : \\.\C:
Fence                       : 3
Clock                       : 130078672846368199
CreateTime                  : 3/15/2013 5:28:04 PM
UpdateTime                  : 3/15/2013 5:28:04 PM
FileHash                    : 173b51c11257a2eb 8c05884560fcfd1d
FileName                    : diskraid.exe
FullPathName                : c:\rf1a\diskraid.exe
Index                       : 1
ReplicatedFolderId          : 997d8f76-1207-49d7-85c9-ded015105a2f

Identifier                  : {DCE7FC28-5584-4D5D-BC84-2BD9D53CC2FC}-v539
Flags                       : 5
Attributes                  : 32
GlobalVersionSequenceNumber : {DCE7FC28-5584-4D5D-BC84-2BD9D53CC2FC}-v539
UpdateSequenceNumber        : 71577024
ParentId                    : {997D8F76-1207-49D7-85C9-DED015105A2F}-v1
FileId                      : 562949953495211
Volume                      : \\.\C:
Fence                       : 3
Clock                       : 130078672846524997
CreateTime                  : 3/15/2013 5:28:04 PM
UpdateTime                  : 3/15/2013 5:28:04 PM
FileHash                    : 6bcd377edf35e621 a7927703c08545d8
FileName                    : diskshadow.exe
FullPathName                : c:\rf1a\diskshadow.exe
Index                       : 2
ReplicatedFolderId          : 997d8f76-1207-49d7-85c9-ded015105a2f
```

该命令用于检索复制组RG01以及已复制文件夹RF1A中，本地计算机与上游服务器SRV02之间未复制的前100个变更。该命令会显示所有文件的元数据信息。

### 示例 2：获取上游计算机和下游计算机之间未复制的更改
```powershell
PS C:\> Get-DfsrBacklog -DestinationComputerName "SRV01" -SourceComputerName "SRV02" -GroupName "RG01" -FolderName "RF1" | Format-Table FullPathName, UpdateTime
```
```output
FullPathName                      UpdateTime
------------                      ----------
c:\rf1a\imageres.dll       3/15/2013 5:28:45 PM
c:\rf1a\mshtml.dll         3/15/2013 5:28:50 PM
```

此命令用于检索复制组RG01及已复制文件夹RF1中，从下游计算机SRV01到上游计算机SRV02之间发生的、尚未被复制的（即未完成复制的）前100个更改记录。该命令还会将输出结果格式化为表格形式，其中仅包含文件路径和修改日期信息（这些信息均来自上游服务器）。

### 示例 3：检索未复制的更改数量以进行显示
```powershell
PS C:\> Get-DfsrBacklog -GroupName "RG01" -FolderName "RF01" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" -Verbose
```
```output
The replicated folder has a backlog of files. Replicated folder: "RF01". Count: 2400
```

此命令用于检索复制组RG01及其复制的文件夹RF01中，下游计算机SRV02与上游计算机SRV01之间未复制的更改的总数。该命令会将输出结果显示在详细信息流（verbose stream）中。

### 示例 4：获取未复制的更改次数，并将其存储到字符串对象中
```powershell
PS C:\> (Get-DfsrBacklog -GroupName "RG01" -FolderName "RF01" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" -Verbose 4>&1).Message.Split(':')[2]
```
```output
2400
```

该命令用于获取复制组RG01及其复制的文件夹RF01中，下游计算机SRV02与上游计算机SRV02之间未复制变更的总数量。命令会将详细的流数据转换为一个仅包含计数的文本字符串，以便后续处理。

### 示例 5：获取文件中未复制的更改数量
```powershell
PS C:\> Get-DfsrBacklog -GroupName "RG01" -FolderName "RF01" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" -Verbose 4> verbose.txt > null
PS C:\> Get-Content .\verbose.txt
```
```output
The replicated folder has a backlog of files. Replicated folder: "RF01". Count: 2400
```

该命令用于获取复制组RG01及其复制的文件夹RF01中，下游计算机SRV02与上游计算机SRV02之间未复制变更的总数量。命令会将详细的流数据转换为一个仅包含计数的文本字符串，以便后续处理。

## 参数

### -DestinationComputerName
指定接收计算机的名称。目标计算机也被称为入站计算机或下游计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReceivingMember, RMem

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -FolderName
指定一组已复制文件夹的名称。如果不指定此参数，该cmdlet将查询所有参与复制的文件夹。您可以指定多个文件夹（用逗号分隔），也可以使用通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RF, RfName

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -GroupName
指定一个复制组名称的数组。如果您不指定此参数，该cmdlet将查询所有参与的复制组。您可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RG, RgName

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -SourceComputerName
指定发送计算机的名称。源计算机也被称为外出（outbound）计算机或上游（upstream）计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SendingMember, SMem

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### Microsoft.DistributedFileSystemReplication.DfsReplicatedFolder

### 字符串

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrIdRecord

## 备注

## 相关链接
