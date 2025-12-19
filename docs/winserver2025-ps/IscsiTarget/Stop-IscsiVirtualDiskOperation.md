---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/stop-iscsivirtualdiskoperation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-IscsiVirtualDiskOperation
---

# 停止 IscsiVirtualDiskOperation 操作

## 摘要
停止在 iSCSI 虚拟磁盘上正在进行的长时间运行操作。

## 语法

### DevicePath（默认值）
```
Stop-IscsiVirtualDiskOperation [-Path] <String> [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

### InputObject
```
Stop-IscsiVirtualDiskOperation -InputObject <IscsiVirtualDisk> [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Stop-IscsiVirtualDiskOperation` cmdlet 用于停止正在 iSCSI 虚拟磁盘上进行的长时间运行的操作。如果您取消某个操作，该操作可能会在取消生效之前完成。在该 cmdlet 完成后，务必重新枚举或重新检查受影响的对象。

停止创建操作可以删除已生成的文件，或者保持文件原样而不将其内容置零。

在您停止某个操作后，需要扩展大小的现有文件的大小可能会暂时显得更大，这种情况会持续到下一次重新启动iSCSI服务、重新启动磁盘，或者禁用并重新启用磁盘为止。在此过程中，部分数据可能会丢失。

如果您停止了一个操作，虚拟磁盘可能会处于不一致的状态，此时需要执行一次新的回滚操作。

这个cmdlet通过使用*InputObject*参数作为管道输入，来接受*ComputerName*和*Path*参数的值。

## 示例

### 示例 1：停止虚拟磁盘操作
```
PS C:\> Stop-IscsiVirtualDiskOperation -Path "D:\VirtualDisk09"
```

此命令会停止虚拟磁盘上指定位置正在进行的操作。

## 参数

### -ComputerName
如果此cmdlet在远程计算机上运行，则指定远程计算机的名称或IP地址。

如果此 cmdlet 在集群配置上运行，则指定集群资源组的网络名称或集群节点的名称。

如果您没有为该参数指定值，cmdlet 将使用本地计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Credential
指定在连接远程计算机时所需的身份凭证（用户名和密码）。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
指定一个 **IscsiVirtualDisk** 对象。您可以使用 **Get-IscsiVirtualDisk** cmdlet 来获取一个 **IscsiVirtualDisk** 对象。

```yaml
Type: IscsiVirtualDisk
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定与 iSCSI 虚拟磁盘关联的虚拟硬盘（VHDX）文件的路径。此cmdlet会停止对所指定的iSCSI虚拟磁盘进行的正在运行的操作。

```yaml
Type: String
Parameter Sets: DevicePath
Aliases: DevicePath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Get-IscsiVirtualDisk](./Get-IscsiVirtualDisk.md)

