---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/backup-dhasconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Backup-DHASConfiguration
---

# 备份DHAS配置

## 摘要
备份配置文件。

## 语法

```
Backup-DHASConfiguration [-Path] <String> [-Force] [<CommonParameters>]
```

## 描述
`Backup-DHASConfiguration` cmdlet 用于从 `web.config` 文件中备份设备健康认证（Device Health Attestation）服务的配置信息。

您必须具有管理员权限才能运行此cmdlet。

## 示例

### 示例 1：备份服务配置
```
PS C:\> Backup-DHASConfiguration -Path "c:\backup.xml"
```

该命令会将服务配置从 `web.config` 文件备份到由 `Path` 参数指定的文件中。

## 参数

### -Force
强制命令运行，而无需请求用户确认。

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

### -Path
指定用于保存备份配置文件的位置。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 字符串
这个cmdlet返回一个包含备份文件路径的字符串。

## 备注

## 相关链接

[ Restore-DHASConfiguration](./Restore-DHASConfiguration.md)

