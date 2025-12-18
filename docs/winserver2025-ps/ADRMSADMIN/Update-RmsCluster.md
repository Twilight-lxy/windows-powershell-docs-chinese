---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/update-rmscluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-RmsCluster
---

# Update-RmsCluster

## 摘要
更新AD RMS集群信息。

## 语法

```
Update-RmsCluster [-Force] [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Update-RmsCluster** cmdlet 用于更新集群信息，包括在 Active Directory 权限管理服务（AD RMS）中定义该集群的内容层次结构。AD RMS 集群的结构会反映在与该集群关联的提供程序驱动器的目录结构中。例如，您可以从 RightsPolicyTemplate 子目录中访问权限策略模板的相关信息。

要更新 AD RMS 集群信息，请将 *Path* 参数设置为 `<PSDrive>:\`，其中 `<PSDrive>` 是与要更新的集群关联的 AD RMS 提供程序驱动器 ID。

## 示例

### 示例 1：更新集群信息
```
PS C:\> Update-RmsCluster -Path "." -Force
```

此命令用于更新 AD RMS 集群的信息。

## 参数

### -Confirm
在运行cmdlet之前会提示您进行确认。

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

### -Force
如果所做的更改不会危及安全性，那么可以忽略那些阻止命令成功执行的限制。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Path
指定一个提供者驱动器以及路径，或者当前驱动器上的相对路径。可以使用点（.）来表示当前位置。此参数不支持通配符，并且没有默认值。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

