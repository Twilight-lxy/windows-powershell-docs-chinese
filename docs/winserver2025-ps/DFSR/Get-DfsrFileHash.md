---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrfilehash?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrFileHash
---

# Get-DfsrFileHash

## 摘要
获取一个文件哈希值。

## 语法

```
Get-DfsrFileHash [-Path] <String[]> [<CommonParameters>]
```

## 描述
`Get-DfsrFileHash` cmdlet 可获取与分布式文件系统（DFS）复制服务在正常复制过程中为指定文件或文件夹计算出的哈希值相同的哈希值。使用此 cmdlet 可以判断您是否正确填充了内容集，或者文件在各个复制节点之间是否已保持同步状态。

## 示例

### 示例 1：获取文件哈希值
```powershell
PS C:\> Get-DfsrFileHash -Path "C:\Rf01\Drawing2.vsd"
```
```output
Path                                                        FileHash
----                                                        --------
C:\Rf01\Drawing2.vsd                                        6EA20E2D-EAA03FE3-22004718-F1D0FCE2
```

此命令使用 **Get-DfsrFileHash** cmdlet 来获取文件 `C:\Rf01\Drawing2.vsd` 的模拟哈希值。

### 示例 2：获取文件夹及其内容的哈希值
```powershell
PS C:\> Get-DfsrFileHash -Path "C:\Rf01\*"
```
```output
Path                                                        FileHash
----                                                        --------
C:\Rf01\archive                                             13B7D499-1D5B4DBF-8800A20D-52CA5845
C:\Rf01\Drawing2.png                                        EA22F7CF-AD58721C-29CB086B-CDE228BC
C:\Rf01\Drawing2.vsd                                        6EA20E2D-EAA03FE3-22004718-F1D0FCE2
```

此命令使用 **Get-DfsrFileHash** cmdlet 来检索文件夹的哈希值以及该文件夹中各个文件的哈希值。

### 示例 3：使用递归方法获取文件夹及其内容的哈希值
```powershell
PS C:\> Get-DfsrFileHash -Path (Get-ChildItem -Path "C:\Rf01" -Recurse).fullname
```
```output
Path                                                        FileHash
----                                                        --------
C:\Rf01\archive                                             13B7D499-1D5B4DBF-8800A20D-52CA5845
C:\Rf01\Drawing2.png                                        EA22F7CF-AD58721C-29CB086B-CDE228BC
C:\Rf01\Drawing2.vsd                                        6EA20E2D-EAA03FE3-22004718-F1D0FCE2
C:\Rf01\archive\Drawing1.png                                A32E700D-E541F7B7-241CD9B3-D1EA9D6C
C:\Rf01\archive\Drawing1.vsd                                DA61DD74-52BDCB8E-2A793467-EB4BCED0
```

这个命令使用 **Get-DfsrFileHash** cmdlet 来获取文件夹的哈希值以及该文件夹中各个文件的哈希值。同时，该命令还利用 **Get-ChildItem** cmdlet 递归地查找路径中的所有文件和文件夹。

### 示例 4：获取带有 *.png 扩展名的文件的哈希值
```powershell
PS C:\> Get-DfsrFileHash -Path (Get-ChildItem -Path "C:\Rf01" -Recurse -Filter *.png ).fullname
```
```output
Path                                                        FileHash
----                                                        --------
C:\Rf01\Drawing2.png                                        EA22F7CF-AD58721C-29CB086B-CDE228BC
C:\Rf01\archive\Drawing1.png                                A32E700D-E541F7B7-241CD9B3-D1EA9D6C
```

这个命令使用 **Get-DfsrFileHash** cmdlet 来检索所有具有 `.png` 扩展名的文件的哈希值。该命令会递归地搜索文件夹路径中的文件。

### 示例 5：检索并比较两个复制文件夹之间的文件哈希值
```powershell
PS C:\> net use x: \\Srv01\c$\Rf01
PS C:\> Get-DfsrFileHash x:\* | Out-File C:\Srv01.txt
PS C:\> net use x: /d
PS C:\> net use x: \\Srv02\e$\data
PS C:\> Get-DfsrFileHash x:\* | Out-File C:\Srv02.txt
PS C:\> net use x: /d
PS C:\> Compare-Object -ReferenceObject (Get-Content C:\Srv01.txt) -DifferenceObject (Get-Content C:\Srv02.txt) -IncludeEqual
```
```output
InputObject                                                 SideIndicator
-----------                                                 -------------
                                                            ==
Path                                                    ... ==
----                                                    ... ==
x:\archive                                              ... ==
x:\Drawing2.vsd                                         ... ==
                                                            ==
                                                            ==
x:\Drawing2.png                                         ... =>
x:\Drawing2.png                                         ... <=
```

这个例子从不同的计算机上检索并比较了两个复制文件夹的模拟文件哈希值。

第一个命令将一个驱动器映射到第一台计算机上的复制文件夹。

第二个命令使用 **Get-DfsrFileHash** cmdlet 来获取文件夹内容的模拟文件哈希值。该命令将输出结果保存到一个文本文件中。

第三个命令会删除第一台计算机上的映射驱动器。

第四条命令将相同的驱动器字母映射到第二台计算机上的复制文件夹上。

第五条命令使用了 **Get-DfsrFileHash** cmdlet 来获取该文件夹内容的模拟文件哈希值，并将输出结果保存到一个文本文件中。

第六条命令会删除第二台计算机上的映射驱动器。

第七条命令使用了 **Compare-Object** cmdlet 来比较这两个输出文件，并显示比较结果。在这个例子中，`Drawing2.png` 文件是不同的。

## 参数

### -Path
指定一个包含文件或文件夹路径的数组。您可以使用本地路径、映射驱动器或 UNC 路径。

如果您使用通配符来指定一个文件或文件夹，此cmdlet会分别计算所有匹配的文件或文件夹。如果您指定的文件夹路径以通配符结尾（例如 C:\Rf01\*），则cmdlet会计算该文件夹中所有内容的哈希值。此参数不支持对子文件夹及其内容进行递归处理。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: FullName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串

## 输出

### DfsrFileHash

## 备注

## 相关链接

