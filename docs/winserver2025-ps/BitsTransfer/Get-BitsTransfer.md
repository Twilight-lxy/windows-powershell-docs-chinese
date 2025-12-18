---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BackgroundIntelligentTransfer.Management.dll-Help.xml
Module Name: BitsTransfer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitstransfer/get-bitstransfer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-BitsTransfer
---

# Get-BitsTransfer

## 摘要
获取与现有的BITS传输作业相关联的BitsJob对象。

## 语法

### ListJobsByName（默认值）
```
Get-BitsTransfer [[-Name] <String[]>] [-AllUsers] [<CommonParameters>]
```

### ListJobsById
```
Get-BitsTransfer [-JobId] <Guid[]> [<CommonParameters>]
```

## 描述
`Get-BitsTransfer` cmdlet 用于检索一组由 Background Intelligent Transfer Service (BITS) 执行的传输任务。默认情况下，该 cmdlet 会返回当前用户拥有的传输任务；不过如果你具有管理员权限，可以指定 `AllUsers` 参数，从而让命令显示所有用户拥有的传输任务。返回的任务可以通过名称或 ID 进行筛选。这些任务由 `BitsJob` 对象表示。

## 示例

### 示例 1：获取当前用户拥有的所有 BitsJob 对象
```
PS C:\> Get-BitsTransfer

JobId                   DisplayName             TransferType            JobState                OwnerAccount
-----                   -----------             ------------            --------                ------------
07acbe90-7d25-4d05-a... TestJob2                Download                Suspended               DOMAIN01\user01
c0dd3d8c-c3a2-4562-8... TestJob1                Download                Transferred             DOMAIN01\user01
1ef8c549-7a92-4173-b... BitsJobTransfer         Download                Transferred             DOMAIN01\user01
2c8302d5-3f44-4981-8... BitsJobTransfer         Download                Transferred             DOMAIN01\user01
```

这个命令可以获取当前用户拥有的所有 **BitsJob** 对象。

### 示例 2：通过作业 ID 获取 BitsJob 对象
```
PS C:\> Get-BitsTransfer -JobId C0DD3D8C-C3A2-4562-8324-80B19224879C

JobId                   DisplayName             TransferType            JobState                OwnerAccount
-----                   -----------             ------------            --------                ------------
c0dd3d8c-c3a2-4562-8... TestJob1                Download                Transferred             DOMAIN01\user01
```

该命令用于获取由指定作业ID标识的**BitsJob**对象。

### 示例 3：获取所有显示名称为特定值的 BitsJob 对象
```
PS C:\> Get-BitsTransfer -AllUsers -Name "*Microsoft*", "*Windows*"

JobId                   DisplayName             TransferType            JobState                OwnerAccount
-----                   -----------             ------------            --------                ------------
07acbe90-7d25-4d05-a... MicrosoftTest           Download                Suspended               DOMAIN01\user01
c0dd3d8c-c3a2-4562-8... WindowsTest             Download                Transferred             DOMAIN01\user02
```

这个命令会获取所有用户拥有的所有 **BitsJob** 对象，其中这些 **BitsJob** 对象的 **DisplayName** 属性包含 “Microsoft” 或 “Windows”。如果用户没有管理员权限，此命令将会返回错误，因为它使用了 *AllUsers* 参数。

### 示例 4：获取由特定显示名称标识的 BitsJob 对象
```
C:\PS>Get-BitsTransfer -Name "TestJob1"

JobId                   DisplayName             TransferType            JobState                OwnerAccount
-----                   -----------             ------------            --------                ------------
c0dd3d8c-c3a2-4562-8... TestJob1                Download                Transferred             DOMAIN01\user01
```

这个命令会获取由指定显示名称标识的 **BitsJob** 对象。

## 参数

### -AllUsers
表示此 cmdlet 会获取所有用户拥有的 BITS 传输作业。如果未指定此参数，则仅返回当前用户拥有的作业。该参数需要管理员凭据。

```yaml
Type: SwitchParameter
Parameter Sets: ListJobsByName
Aliases: all

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -JobId
通过作业ID指定一个BITS作业数组。只有包含在该数组中的BITS作业才会被返回。如果将**BitsJob**对象传递给此cmdlet，那么这些对象的作业ID将作为该参数的值使用。

```yaml
Type: Guid[]
Parameter Sets: ListJobsById
Aliases: id

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
根据作业名称指定一个BITS作业数组。只有那些名称与该数组中的某个名称匹配的BITS作业才会被返回。您可以使用标准的通配符，如星号（*）和问号（？），也可以使用范围操作符，例如“\[a-r\]”。

例如，您可以使用以下任意命令：

`Get-BitsTransfer -Name "BITS*"`

`Get-BitsTransfer -Name "BITS Transfer"`

`Get-BitsTransfer -Name "BITS Transfer[a-r]"`

也可以将通配符和范围操作符结合起来使用。

```yaml
Type: String[]
Parameter Sets: ListJobsByName
Aliases: n

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.BackgroundIntelligentTransfer.Management.BitsJob[]
此cmdlet接受一个或多个**BitsJob**对象作为输入，这些对象会根据属性名称填充JobId参数。

## 输出

### Microsoft.BackgroundIntelligentTransfer.Management.BitsJob[]
这个cmdlet会生成与检索到的BITS传输作业相关联的**BitsJob**对象。

## 备注

## 相关链接

[Add-BitsFile](./Add-BitsFile.md)

[Complete-BitsTransfer](./Complete-BitsTransfer.md)

[Remove-BitsTransfer](./Remove-BitsTransfer.md)

[Resume-BitsTransfer](./Resume-BitsTransfer.md)

[Set-BitsTransfer](./Set-BitsTransfer.md)

[开始比特传输](./Start-BitsTransfer.md)

[Suspend-BitsTransfer](./Suspend-BitsTransfer.md)

