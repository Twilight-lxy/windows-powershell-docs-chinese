---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/convert-iscsivirtualdisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Convert-IscsiVirtualDisk
---

# 将Iscsi虚拟磁盘转换为其他格式

## 摘要
将一个 iSCSI 虚拟磁盘转换为采用 4K 扇区对齐的高级虚拟磁盘 1.0 格式。

## 语法

```
Convert-IscsiVirtualDisk [-Path] <String> [-DestinationPath] <String> [<CommonParameters>]
```

## 描述
注意：此cmdlet已被弃用，可能在未来的版本中被移除。我们建议您不要使用该cmdlet。

**Convert-IscsiVirtualDisk** cmdlet 将 iSCSI 虚拟磁盘转换为 4K 扇区对齐的高级虚拟磁盘 1.0 格式。如果尝试加载由 iSCSI Target 3.3 创建的 VHD，必须通过运行此 cmdlet 来转换该 VHD。此 cmdlet 同时执行复制和转换操作。可以指定源路径和目标路径为远程文件共享或本地路径。

注意：如果将 iSCSI 目标 3.3 中的差分虚拟磁盘迁移至 Windows Server 2012 R2 的差分虚拟磁盘，请使用此 cmdlet。

## 示例

### 示例 1：转换 VHD 文件
```
PS C:\> Convert-IscsiVirtualDisk -Path "\\zamfirsvr\VHDs\test.vhdx" -DestinationPath "\\win8svr\VHDs\test.vhdx"
```

这个示例会将名为 `test.vhdx` 的 VHD 文件从 `\\\zamfirsvr\VHDs\` 复制并转换为 `\\\win8svr\VHDs\`。转换完成后，就可以加载这个 `test.vhdx` 文件了。

## 参数

### -DestinationPath
指定要复制和转换的 iSCSI 虚拟磁盘的目标路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定与iSCSI虚拟磁盘关联的虚拟硬盘（VHD）文件的路径。可以使用此参数来过滤iSCSI虚拟磁盘对象。

```yaml
Type: String
Parameter Sets: (All)
Aliases: DevicePath

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Checkpoint-IscsiVirtualDisk](./Checkpoint-IscsiVirtualDisk.md)

[Get-IscsiVirtualDisk](./Get-IscsiVirtualDisk.md)

[导入 iSCSI 虚拟磁盘](./Import-IscsiVirtualDisk.md)

[New-IscsiVirtualDisk](./New-IscsiVirtualDisk.md)

[删除Iscsi虚拟磁盘](./Remove-IscsiVirtualDisk.md)

[Restore-IscsiVirtualDisk](./Restore-IscsiVirtualDisk.md)

[Set-IscsiVirtualDisk](./Set-IscsiVirtualDisk.md)

