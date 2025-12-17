---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/restore-caroleservice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Restore-CARoleService
---

# 恢复CARole服务

## 摘要
恢复CA数据库和私钥信息。

## 语法

### 关键点（Key）
```
Restore-CARoleService [-Path] <String> [-Force] [-KeyOnly] [-Password <SecureString>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 数据库
```
Restore-CARoleService [-Path] <String> [-Force] [-DatabaseOnly] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 全部
```
Restore-CARoleService [-Path] <String> [-Force] [-Password <SecureString>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Restore-CARoleService` cmdlet 用于恢复证书颁发机构（CA）的数据库及私钥信息。

## 示例

### 示例 1：恢复根证书颁发机构（CA）的私钥和证书
```
PS C:\> Restore-CARoleService -Path "C:\CABackup"
```

此命令从指定路径恢复CA私钥和证书。

#### 示例 2：仅恢复 CA 数据库
```
PS C:\> Restore-CARoleService -Path "C:\CABackup" -DatabaseOnly
```

此命令从指定的路径恢复CA数据库。该命令不会恢复CA私钥信息。

### 示例 3：仅恢复 CA 密钥
```
PS C:\> Restore-CARoleService -Path "C:\CABackup" -KeyOnly
```

此命令将CA私钥信息恢复到指定的路径。该命令不会恢复CA数据库的数据。

## 参数

### -Confirm
在运行 cmdlet 之前会提示您确认操作。

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

### -DatabaseOnly
表示该cmdlet仅恢复证书颁发机构数据库。

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
强制命令运行，而无需请求用户确认。

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

### -KeyOnly
表示该cmdlet仅恢复证书颁发机构的私钥和证书。

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
指定一个密码（以安全字符串的形式），用于访问私钥和证书信息。要生成一个安全字符串，请使用 [ConvertTo-SecureString](https://go.microsoft.com/fwlink/?LinkID=113291) cmdlet。有关更多信息，请输入 `Get-Help ConvertTo-SecureString`。

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
指定 cmdlet 用于恢复证书颁发机构（CA）数据库和私钥的目录。该 cmdlet 会从您在备份 CA 数据库时所指定的路径中的 “Database” 子目录中恢复数据库文件；同时，它还会从同一路径下的 “Database” 子目录中备份的 .p12 文件中恢复私钥文件。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

### System.String

### System.ManagementAutomation.SwitchParameter

### System.security.SecureString

## 输出

### System Void

## 备注

## 相关链接

[Backup-CARoleService](./Backup-CARoleService.md)

