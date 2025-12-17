---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-addccloningexcludedapplicationlist?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADDCCloningExcludedApplicationList
---

# 获取被排除在克隆应用程序列表之外的应用程序列表

## 摘要
获取该域控制器上已安装的程序和服务的列表，这些程序和服务不在默认的或用户定义的包含列表中。

## 语法

### 默认值（Default）
```
Get-ADDCCloningExcludedApplicationList [<CommonParameters>]
```

### XML
```
Get-ADDCCloningExcludedApplicationList [-Force] [-GenerateXml] [-Path <String>] [<CommonParameters>]
```

## 描述
**Get-ADDCCloningExcludedApplicationList** 这个 cmdlet 会在本地域控制器中搜索那些未包含在默认列表或用户自定义的允许列表中的程序和服务。如果确定这些应用程序支持克隆操作，可以将它们添加到用户自定义的排除列表中；如果不支持克隆，则应在创建克隆介质之前将这些应用程序从源域控制器中删除。任何出现在 cmdlet 输出结果中但未被包含在用户自定义允许列表中的应用都会导致克隆操作失败。

一旦您授予了源虚拟化域控制器被克隆的权限，就需要首先运行 `Get-ADDCCloningExcludedApplicationList` cmdlet，此时不需要为源虚拟化域控制器提供任何额外参数，该命令会列出所有需要评估是否适合克隆的程序或服务。接下来，请与您的软件供应商核对返回的列表，并从其中移除那些无法安全克隆的应用程序。最后，您可以再次运行 `Get-ADDCCloningExcludedApplicationList` cmdlet，并使用 `GenerateXml` 参数集来生成 `CustomDCCloneAllowList.xml` 文件。

在使用 `New-ADDCCloneConfigFile` cmdlet 之前，需要先运行 `Get-ADDCCloningExcludedApplicationList` cmdlet。因为如果 `New-ADDCCloneConfigFile` cmdlet 检测到有被排除的应用程序，那么它将不会创建 DCCloneConfig.xml 文件。

## 示例

### 示例 1：将被排除的应用程序列表显示到控制台
```
PS C:\> Get-ADDCCloningExcludedApplicationList
```

此命令会将被排除的应用程序列表显示在控制台上。如果系统中已经存在一个 `CustomDCCloneAllowList.xml` 文件，那么该 cmdlet 会显示该文件与操作系统中的应用程序列表之间的差异；如果两个列表完全相同，那么显示的结果可能为空（即没有差异）。

### 示例 2：生成被排除的应用程序列表并将其保存为文件
```
PS C:\> Get-ADDCCloningExcludedApplicationList -GenerateXml -Path C:\Windows\NTDS -Force
```

此命令会将排除的应用程序列表生成为一个名为 `CustomDCCloneAllowList.xml` 的文件，并将其保存在指定的文件夹路径 `C:\Windows\NTDS` 下。如果在该路径位置已经存在同名文件，系统会强制覆盖该旧文件。

## 参数

### -Force
强制命令运行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: Xml
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GenerateXml
该参数用于指示是否创建 `CustomDCCloneAllowList.xml` 文件，并将其写入通过 `Path` 参数指定的位置。

```yaml
Type: SwitchParameter
Parameter Sets: Xml
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定在使用*GenerateXml*参数创建CustomDCCloneAllowList.xml文件时所使用的文件夹路径。

```yaml
Type: String
Parameter Sets: Xml
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

### 无

## 输出

### 实体（Entity）

## 备注

## 相关链接

[New-ADDCCloneConfigFile](./New-ADDCCloneConfigFile.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

