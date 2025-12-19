---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPointVdi.dll-Help.xml
Module Name: MultiPointVdi
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipointvdi/new-wmsvirtualdesktoptemplate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-WmsVirtualDesktopTemplate
---

# 新WMS虚拟桌面模板

## 摘要
创建一个虚拟桌面模板。

## 语法

### NonDomainJoin
```
New-WmsVirtualDesktopTemplate -InputFilePath <String> [-VhdLocation <String>] -TemplatePrefix <String>
 -AdministratorUser <String> -AdministratorPassword <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### DomainJoin
```
New-WmsVirtualDesktopTemplate -InputFilePath <String> [-VhdLocation <String>] -TemplatePrefix <String>
 -AdministratorUser <String> -Domain <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**New-WmsVirtualDesktopTemplate** cmdlet 根据一个具有相同名称的现有模板来关闭所有工作站上的虚拟桌面。随后，它会使用通过 **Import-WmsVirtualDesktop** 创建的虚拟硬盘来生成一个新的虚拟桌面模板。该虚拟桌面属于某个工作组，或者被连接到所提供的域中，并且配置有一个具有指定用户名和密码的管理账户。

## 示例

#### 示例 1：创建一个虚拟桌面模板
```
PS C:\> New-WmsVirtualDesktopTemplate -InputFilePath "C:\Images\Windows10Enterprise.iso" -TemplatePrefix "MyVdiImage" -VhdLocation "C:\MultiPointVhdImages" -AdministratorUser "admin" -AdministratorPassword "password"
```

这个命令创建了一个虚拟桌面模板，您可以根据需要进行自定义，或者使用它来生成新的工作站虚拟桌面。

## 参数

### -AdministratorPassword
指定要分配给管理员账户的密码。

```yaml
Type: String
Parameter Sets: NonDomainJoin
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AdministratorUser
指定要在虚拟桌面模板中创建的用户的名称，该用户将具有管理员权限。

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

### -Domain
指定虚拟桌面对应的 Active Directory 域的名称。

```yaml
Type: String
Parameter Sets: DomainJoin
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputFilePath
指定用于虚拟桌面模板的输入文件的完整路径。有效的文件类型包括.wim、.iso或.vhd，这些文件包含将用作客户端操作系统的Windows版本。

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

### -TemplatePrefix
指定用于虚拟机模板名称的前缀。

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

### -VhdLocation
指定用于存储桌面模板文件以及station.vhd文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

