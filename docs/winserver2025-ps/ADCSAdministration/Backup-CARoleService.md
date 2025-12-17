---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/backup-caroleservice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Backup-CARoleService
---

# 备份-CARoleService

## 摘要
备份CA数据库和私钥信息。

## 语法

### 关键点
```
Backup-CARoleService [-Path] <String> [-Force] [-KeyOnly] [-Password <SecureString>] [<CommonParameters>]
```

### 数据库
```
Backup-CARoleService [-Path] <String> [-Force] [-DatabaseOnly] [-Incremental] [-KeepLog] [<CommonParameters>]
```

### 全部
```
Backup-CARoleService [-Path] <String> [-Force] [-Password <SecureString>] [-Incremental] [-KeepLog]
 [<CommonParameters>]
```

## 描述
`Backup-CARoleService` cmdlet 将证书颁发机构（CA）的数据库和私钥信息备份到指定的路径。

## 示例

#### 示例 1：备份 CA 数据库和私钥信息
```
PS C:\> Backup-CARoleService -Path "C:\CABackup"
```

此命令将CA数据库和私钥信息导出到指定的路径。

#### 示例 2：仅备份 CA 数据库
```
PS C:\> Backup-CARoleService -Path "C:\CABackup" -DatabaseOnly
```

此命令将CA数据库导出到指定的路径。该命令不会备份CA私钥信息。

### 示例 3：仅备份 CA 密钥
```
PS C:\> Backup-CARoleService -Path "C:\CABackup" -KeyOnly
```

此命令将CA私钥信息导出到指定的路径。该命令不会备份CA数据库。

## 参数

### -DatabaseOnly
表示该cmdlet仅备份证书颁发机构（CA）数据库。

```yaml
Type: SwitchParameter
Parameter Sets: Database
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force
强制命令执行，而无需请求用户确认。

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

### -Incremental
表示该cmdlet执行增量数据库备份操作。

```yaml
Type: SwitchParameter
Parameter Sets: Database, All
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeepLog
表示该cmdlet不会截断数据库日志。

```yaml
Type: SwitchParameter
Parameter Sets: Database, All
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeyOnly
表示该cmdlet仅备份CA私钥和证书。

```yaml
Type: SwitchParameter
Parameter Sets: Key
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Password
指定一个密码（以安全字符串的形式），用于保护私钥和证书信息。要生成一个安全字符串，请使用 [ConvertTo-SecureString](https://go.microsoft.com/fwlink/?LinkID=113291) cmdlet。有关更多信息，可以输入 `Get-Help ConvertTo-SecureString`。

```yaml
Type: SecureString
Parameter Sets: Key, All
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
指定该 cmdlet 将 CA 数据库和私钥备份到的目录。如果备份数据库，cmdlet 会创建一个名为 “Database” 的新子目录来存放数据库备份文件；如果备份私钥，cmdlet 会将私钥写入到您指定的路径中 “Database” 子目录下的 .p12 文件中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.ManagementAutomation.SwitchParameter

### System.Security.SecureString

## 输出

### SystemVoid

## 备注

## 相关链接

[ConvertTo-SecureString](https://go.microsoft.com/fwlink/?LinkID=113291)

[Restore-CARoleService](./Restore-CARoleService.md)

